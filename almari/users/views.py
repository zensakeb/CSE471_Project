from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_backends
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from users.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages
from .models import CustomUser, CartItem, UserActionLog
from social_django.utils import psa
from .forms import UserUpdateForm  # Import the form
from django.contrib.auth.models import User
from .supabase_client import supabase
import uuid



# Custom LoginView
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_nav'] = True
        return context
    def get_success_url(self):
        user = self.request.user
        if user.is_superuser:
            return reverse_lazy('users:admin_dashboard')
        return reverse_lazy('users:frontpage')

    
def authView(request):
    # Handle your authentication (sign up) logic here
    return render(request, 'registration/signup.html')

@login_required
def frontpage(request):
    return render(request, 'core/frontpage.html', {
        'user_id': request.user.id,
        'username': request.user.username,
    })


# Profile View
@login_required
def profile(request):
    return render(request, 'core/frontpage.html')


# Edit Profile View
@login_required
def edit_profile(request, user_id=None):
    if user_id:
        user = get_object_or_404(CustomUser, id=user_id)
        is_admin_editing = (user != request.user and request.user.is_staff)
        if not is_admin_editing and user != request.user:
            return redirect('users:profile')
    else:
        user = request.user
        is_admin_editing = False

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            if is_admin_editing:
                return redirect('users:admin_dashboard')  # ✅ admin goes back to dashboard
            else:
                return redirect('users:frontpage')  # ✅ normal user goes to frontpage
        else:
            print("Form errors:", form.errors)
    else:
        form = UserUpdateForm(instance=user)

    return render(request, 'users/edit_profile.html', {
        'form': form,
        'user': user,
        'hide_nav': True
    })

# User Deactivation View
@login_required
@user_passes_test(lambda u: u.is_superuser)
def deactivate_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_active = False
    user.save()
    messages.success(request, f'User {user.username} has been deactivated.')
    return redirect('users:admin_dashboard')


# User Activation View
@login_required
@user_passes_test(lambda u: u.is_superuser)
def activate_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_active = True
    user.save()
    messages.success(request, f'User {user.username} has been activated.')
    return redirect('users:admin_dashboard')


# Custom LogoutView
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')  # where to go after logout

    def get(self, request, *args, **kwargs):
        """Override GET to allow logout via a simple link"""
        return self.post(request, *args, **kwargs)
    
# Admin Dashboard View   
@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    search_query = request.GET.get('search', '')
    if search_query:
        users = CustomUser.objects.filter(username__icontains=search_query) | CustomUser.objects.filter(email__icontains=search_query)
    else:
        users = CustomUser.objects.all()

    now = timezone.localtime(timezone.now())
    # Get the current time in the user's timezone
    return render(request, 'users/admin_dashboard.html', {
        'users': users,
        'now': now,
        'hide_nav': True
    })

# Google Login View (if using social auth)
@psa('social:complete')
def google_login(request, *args, **kwargs):
    # Logic for Google OAuth login
    pass

# users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from .supabase_client import supabase
import uuid

import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import CustomUser
from .supabase_client import supabase

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)

            image = request.FILES.get('profile_image')
            if image:
                # Generate a unique filename
                ext = image.name.rsplit('.', 1)[-1].lower()
                image_name = f"{uuid.uuid4()}.{ext}"
                file_path = f"profiles/{image_name}"

                # Read the uploaded file into bytes
                data = image.read()

                # Upload bytes to Supabase
                res = supabase.storage.from_('user-profile-images') \
                           .upload(file_path, data, {'content-type': image.content_type})
                if hasattr(res, 'error') and res.error:
                    print("Upload failed:", res.error)
                else:
                    # Retrieve public URL and save it
                    public_url = supabase.storage.from_('user-profile-images') \
                            .get_public_url(file_path)
                    user.profile_image = public_url


            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect('users:login')
        else:
            messages.error(request, 'Error creating account. Please try again.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {
        'form': form,
        'hide_nav': True,
    })


def my_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)  # Assuming CartItem has a user field
    return render(request, 'users/my_cart.html', {'cart_items': cart_items})

def checkout(request):
    return render(request, 'users/checkout.html')


@login_required
def add_to_cart(request, project_id):
    project = get_object_or_404(Project, id=project_id)  # Ensure we get a Project
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=project)  # Link cart item to project

    if not created:
        cart_item.quantity += 1  # Increase quantity if the item already exists
        cart_item.save()

    return redirect('users:my_cart')  # Redirect to cart after adding

@login_required
def remove_from_cart(request, project_id):
    cart_item = CartItem.objects.filter(user=request.user, product_id=project_id).first()  # Get cart item
    if cart_item:
        cart_item.delete()  # Remove from cart if exists
    return redirect('users:my_cart')


@login_required
def increase_quantity(request, product_id):
    cart_item = get_object_or_404(CartItem, user=request.user, product_id=product_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('users:my_cart')

@login_required
def decrease_quantity(request, product_id):
    cart_item = get_object_or_404(CartItem, user=request.user, product_id=product_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()  # optional: remove item if quantity hits 0
    return redirect('users:my_cart')

def some_interaction_view(request):
    if request.user.is_authenticated:
        UserActionLog.objects.create(user=request.user, action="Clicked 'Buy Now'")
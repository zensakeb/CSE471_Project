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
from .models import CustomUser
from social_django.utils import psa
from .forms import UserUpdateForm  # Import the form
from django.contrib.auth.models import User



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
        return reverse_lazy('users:profile')
    
def authView(request):
    # Handle your authentication (sign up) logic here
    return render(request, 'registration/signup.html')

def frontpage(request):
    return render(request, 'core/frontpage.html')

# Profile View
@login_required
def profile(request):
    return render(request, 'core/frontpage.html')


# Edit Profile View
@login_required
def edit_profile(request, user_id=None):
    if user_id:
        # Retrieve the user based on user_id
        user = get_object_or_404(CustomUser, id=user_id)
        if not request.user.is_staff:  # Ensure that only admins can edit others' profiles
            return redirect('users:profile')  # Redirect if the logged-in user is not an admin
    else:
        user = request.user  # Default to the logged-in user
    
    if request.method == 'POST':
        # Pass the correct user instance to the form
        form = UserUpdateForm(request.POST, instance=user)
        print("Form data:", request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('users:profile')  # Redirect to the profile page after successful edit
        else:
            print("Form errors:", form.errors)  # Debugging line to check form errors
    else:
        # Pass the correct user instance to the form
        form = UserUpdateForm(instance=user)

    return render(request, 'users/edit_profile.html', {'form': form, 'user': user, 'hide_nav': True})

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

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('users:login')  # Redirect to login after successful signup
        else:
            messages.error(request, 'Error creating account. Please try again.')

    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form, 'hide_nav': True})
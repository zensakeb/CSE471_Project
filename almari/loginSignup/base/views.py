from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_backends
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm  # Assuming you have a custom user creation form

@login_required
def home(request):
 return render(request, "core/frontpage.html", {})


def authView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = form.save()
            user.backend = get_backends()[0].__module__ + "." + get_backends()[0].__class__.__name__
            login(request, user)
            return redirect('core:frontpage')  # or wherever you want
        else:
            print(form.errors)  # Print form errors to console for debugging
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Use AuthenticationForm
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('core:frontpage')  # Redirect to the front page after login
        else:
            return render(request, 'registration/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()  # Initialize an empty form for GET request
    return render(request, 'registration/login.html', {'form': form})

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('password_change_done')

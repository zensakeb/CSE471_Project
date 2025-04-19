from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

@login_required
def home(request):
 return render(request, "core/frontpage.html", {})


def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST)
  if form.is_valid():
    user = form.save()  # Save the user
    # Log the user in immediately after signup
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password1')
    user = authenticate(username=username, password=password)
    login(request, user)
    return redirect('core:frontpage')  # Redirect to frontpage after login
  else:
    form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:frontpage')  # Redirect to the front page after login
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('password_change_done')

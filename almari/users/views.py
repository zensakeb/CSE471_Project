from django.shortcuts import render

# Create your views here.
# almari/users/views.py

from django.shortcuts import render

def profile(request):
    # renders a template at users/templates/users/profile.html
    return render(request, 'users/profile.html')

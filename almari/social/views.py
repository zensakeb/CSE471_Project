from django.shortcuts import render

# Create your views here.
# almari/social/views.py

from django.shortcuts import render

def login_view(request):
    return render(request, 'social/login.html')  # Make sure to create this template

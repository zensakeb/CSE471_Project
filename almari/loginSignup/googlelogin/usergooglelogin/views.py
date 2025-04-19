from django.shortcuts import render, redirect
from django.contrib.auth import logout

from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

def google_login(request):
    # Replace with your actual logic
    return redirect("https://accounts.google.com/o/oauth2/auth")


def google_callback(request):
    return HttpResponse("This is the Google callback.")

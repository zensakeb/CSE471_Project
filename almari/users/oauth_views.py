from django.shortcuts import render, redirect
from social_django.utils import psa

@psa('social:complete')
def google_login(request, *args, **kwargs):
    # Logic for Google OAuth login
    pass

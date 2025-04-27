# core/urls.py
from django.urls import path
from .views import frontpage, social_wall

app_name = 'core'

urlpatterns = [
    path('', frontpage, name='frontpage'),  # This makes the URL for frontpage view
    path('social-wall/', social_wall, name='social_wall'),  # URL pattern for social wall
]


# almari/users/urls.py

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # example: user profile or dashboard
    path('', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]

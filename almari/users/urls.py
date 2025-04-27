# almari/users/urls.py

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.profile, name='view_profile'),  # Changed to be more explicit
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]

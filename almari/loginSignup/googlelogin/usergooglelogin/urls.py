from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.google_login, name="google_login"),  # or login_view if defined
    path("callback/", views.google_callback, name="google_callback"),  # if needed
]


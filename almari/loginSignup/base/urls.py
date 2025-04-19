from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'base'

urlpatterns = [
    path("", views.home, name="home"),  # Home page route
    path("signup/", views.authView, name="authView"),  # Signup page
    path("login/", views.login_view, name="login"),  # Add this for login page
    # Password change routes
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('google/', include('loginSignup.googlelogin.usergooglelogin.urls')),  # Google login
]

from django.urls import path, include
from .views import authView, home, CustomPasswordChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
 path("", home, name="home"),
 path("signup/", authView, name="authView"),
 path("accounts/", include("django.contrib.auth.urls")),
 # Password change
 path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
 path(
    'password_change/done/',
    auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"),
    name='password_change_done'
),

 path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
 path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


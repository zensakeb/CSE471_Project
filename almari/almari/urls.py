from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views  # Make sure to import auth_views
from users.views import CustomLoginView  # Adjust path if needed
from django.shortcuts import redirect
from projects.views import frontpage

# Add a custom view to handle redirection from '/' to the login page
def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    # Redirect root URL to login page
    path('', redirect_to_login, name='home'),  # This ensures the homepage redirects to login

    path('admin/', admin.site.urls),
    # path('api/', include('orders.urls')),
    # path('orders/', include('orders.urls')),
    # path('social/', include('social.urls')),
    path('users/', include('users.urls', namespace='users')),
    # path('customizer/', include('customizer.urls')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('auth/login/', CustomLoginView.as_view(), name='login'),
    path('auth/google/', include('loginSignup.googlelogin.usergooglelogin.urls')),
    path('auth/social/', include('social_django.urls', namespace='social_auth')),
    path('googlelogin/', include('loginSignup.googlelogin.usergooglelogin.urls')),
    # Password reset paths
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

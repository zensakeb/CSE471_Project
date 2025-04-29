from django.urls import path
from .views import CustomLoginView, CustomLogoutView, profile, edit_profile, admin_dashboard, deactivate_user, activate_user, signup_view
from .oauth_views import google_login
from . import views

app_name = 'users'

urlpatterns = [
<<<<<<< HEAD
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('edit-profile/<int:user_id>', edit_profile, name='edit_profile'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('deactivate/<int:user_id>/', deactivate_user, name='deactivate_user'),
    path('activate/<int:user_id>/', activate_user, name='activate_user'),
    path('google/login/', google_login, name='google_login'),  # If using Google login
    path('frontpage/', views.frontpage, name='frontpage'),
=======
    path('profile/', views.profile, name='view_profile'),  # Changed to be more explicit
    path('edit_profile/', views.edit_profile, name='edit_profile'),
>>>>>>> 5df4f2df0734fccee54bb6b324586aa9d0d8b5cc
]

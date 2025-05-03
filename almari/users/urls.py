from django.urls import path
from .views import CustomLoginView, CustomLogoutView, profile, edit_profile, admin_dashboard, deactivate_user, activate_user, signup_view
from .oauth_views import google_login
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('edit_profile/<int:user_id>', edit_profile, name='edit_profile'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('deactivate/<int:user_id>/', deactivate_user, name='deactivate_user'),
    path('activate/<int:user_id>/', activate_user, name='activate_user'),
    path('google/login/', google_login, name='google_login'),  # If using Google login
    path('frontpage/', views.frontpage, name='frontpage'),
    path('profile/', views.profile, name='view_profile'),  # Changed to be more explicit
    path('my-cart/', views.my_cart, name='my_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/increase/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),

]

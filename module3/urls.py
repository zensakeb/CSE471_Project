from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('track_orders')),
    path('admin/', admin.site.urls),
    path('orders/', include('order_processing.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # ✅ built-in login, logout, password reset
]

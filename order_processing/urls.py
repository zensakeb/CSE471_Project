from django.urls import path
from . import views

urlpatterns = [
    path('track/', views.track_orders, name='track_orders'),
    path('history/', views.order_history, name='order_history'),
]

from django.urls import path
from .views import OrderStatusView, OrderHistoryView

urlpatterns = [
    path('orders/status/<int:user_id>/', OrderStatusView.as_view(), name='order_status'),
    path('orders/history/<int:user_id>/', OrderHistoryView.as_view(), name='order_history'),
]

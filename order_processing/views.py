from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def track_orders(request):
    # Filter out only active orders (exclude delivered or cancelled)
    orders = Order.objects.filter(user=request.user).exclude(status__in=['delivered', 'cancelled']).order_by('-created_at')
    return render(request, 'track_orders.html', {'orders': orders})  # ✅ updated path

@login_required
def order_history(request):
    past_orders = Order.objects.filter(
        user=request.user, 
        status__in=['delivered', 'cancelled']
    ).order_by('-created_at')
    return render(request, 'order_history.html', {'orders': past_orders})  # ✅ updated path

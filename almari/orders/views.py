from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer

class OrderStatusView(APIView):
    def get(self, request, user_id):
        orders = Order.objects.filter(user_id=user_id).exclude(status='cancelled')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OrderHistoryView(APIView):
    def get(self, request, user_id):
        orders = Order.objects.filter(user_id=user_id, status__in=['delivered', 'cancelled'])
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

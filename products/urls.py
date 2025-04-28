# almari/products/urls.py

from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # Example route: listing all products
    path('', views.product_list, name='list'),
    # You can add more, e.g. detail page:
    # path('<int:pk>/', views.product_detail, name='detail'),
]
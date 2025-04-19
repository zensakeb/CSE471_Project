# core/urls.py
from django.urls import path
from .views import frontpage

urlpatterns = [
    path('', frontpage, name='frontpage'),  # This makes the URL for frontpage view
]


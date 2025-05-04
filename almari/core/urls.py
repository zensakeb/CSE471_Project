# core/urls.py
from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path("", views.frontpage, name="frontpage"),


]


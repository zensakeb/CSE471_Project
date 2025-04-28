from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.upload_custom_product, name='upload_custom_product'),  

    path('upload/', views.upload_custom_product, name='upload_custom_product'),
    path('projects/', views.user_projects, name='user_projects'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('projects/delete/<int:pk>/', views.delete_project, name='delete_project'),
    path('projects/edit/<int:pk>/', views.edit_project, name='edit_project'),

]

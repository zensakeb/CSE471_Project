from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from projects.models import Project

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_image = models.URLField(blank=True, null=True)    
    google_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)  # Link to the Project model
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.title} - {self.quantity}"

    @property
    def total_price(self):
        return self.quantity * self.product.price  # Assuming Project has a price field

class UserActionLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
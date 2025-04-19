from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    PRODUCT_TYPES = [
        ('tshirt', 'T-Shirt'),
        ('mug', 'Mug'),
        ('poster', 'Poster'),
    ]
    name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=50, choices=PRODUCT_TYPES)
    base_image = models.ImageField(upload_to='base_products/')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  

    def __str__(self):
        return self.name

class CustomProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    artwork = models.ImageField(upload_to='user_artworks/')
    canvas_data = models.TextField()  # for storing customization JSON
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s {self.product.name}"
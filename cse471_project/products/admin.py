from django.contrib import admin

# Register your models here.
from .models import Category, Order, Review, SocialWallPost

# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
# admin.site.register(OrderItem)
admin.site.register(Review)
admin.site.register(SocialWallPost)

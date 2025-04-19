from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    google_id = models.CharField(max_length=100, null=True, blank=True)

    # Add these two lines to fix reverse accessor conflicts
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',
        blank=True
    )

    def __str__(self):
        return self.username

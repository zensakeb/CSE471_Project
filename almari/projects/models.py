# projects/models.py
from django.db import models
from django.conf import settings

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('mens_clothing','Men’s Clothing'),
        ('womens_clothing','Women’s Clothing'),
        ('childs_clothing','Child’s Clothing'),
        ('mens_shoes','Men’s Shoes'),
        ('womens_shoes','Women’s Shoes'),
        ('childs_shoes','Child’s Shoes'),
        ('mens_accessories','Men’s Accessories'),
        ('womens_accessories','Women’s Accessories'),
    ]

    title       = models.CharField(max_length=200)
    description = models.TextField()
    category    = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    quantity    = models.PositiveIntegerField(default=1)
    tags        = models.CharField(max_length=200, help_text="Comma-separated tags")
    # models.py
    image_url = models.URLField(blank=True, null=True)

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE,
                                    related_name='projects')

    def __str__(self):
        return self.title

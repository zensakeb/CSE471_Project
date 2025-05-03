from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import mark_safe
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'profile_image_tag', 'is_staff', 'is_active']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('phone', 'address', 'profile_image', 'google_id')
        }),
    )

    def profile_image_tag(self, obj):
        if obj.profile_image:
            return mark_safe(
                f'<img src="{obj.profile_image.url}" width="40" height="40" style="border-radius:50%;" />'
            )
        return "-"
    
    profile_image_tag.short_description = 'Profile Image'

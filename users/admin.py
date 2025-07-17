from django.contrib import admin
from .models import User  # Assuming you have a User model in users/models.py

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_active', 'is_staff')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('is_active', 'is_staff')
    ordering = ('last_name', 'first_name')
"""User admin classes."""

# Django
from django.contrib import admin

# Models
from apps.users.models import (User, Manager)


class UserAdmin(admin.ModelAdmin):
    """Add profile admin to base user admin."""

    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'manager',
    )


class ManagerAdmin(admin.ModelAdmin):
    """Add profile admin to base user admin."""

    list_display = (
        'id',
        'user',
    )


admin.site.register(User, UserAdmin)
admin.site.register(Manager, ManagerAdmin)

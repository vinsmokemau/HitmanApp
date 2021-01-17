"""Hit admin classes."""

# Django
from django.contrib import admin

# Models
from apps.hits.models import Hit


admin.site.register(Hit)

"""User model"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from apps.utils.models import BaseModel


class User(BaseModel, AbstractUser):

    """
    User model.
    
    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    is_active = models.BooleanField(
        'status',
        default=True,
    )

    biography = models.TextField(max_length=500, blank=True)

    is_manager = models.BooleanField(
        'manager',
        default=False,
    )

    manager = models.ForeignKey(
        'manager.Manger',
        related_name='lackeys',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        """Return username."""
        return self.username

    def get_absolute_url(self):
        return ('')

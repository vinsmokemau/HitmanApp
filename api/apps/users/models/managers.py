"""Manager model"""

# Django
from django.db import models

# Utilities
from apps.utils.models import BaseModel


class Manager(BaseModel):
    """
    Manager model.
    
    Model to store specific data of the managers (now or in the future)
    """

    user = models.OneToOneField(
        'users.User',
        related_name='as_manager',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managers"

    def __str__(self):
        return str(self.user)

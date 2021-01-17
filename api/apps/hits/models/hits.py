"""User model"""

# Django
from django.db import models

# Utilities
from apps.utils.models import BaseModel


class Hit(BaseModel):
    """
    Hit model.
    
    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    STATUS_CHOICES = (
        ('Assigned', 'Assigned'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    )

    hitman = models.ForeignKey(
        'users.User',
        related_name='hits',
        on_delete=models.CASCADE,
    )
    target = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=50,
        default='Assigned',
    )
    creator = models.ForeignKey(
        'users.User',
        related_name='created_hits',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Hit"
        verbose_name_plural = "Hits"

    def __str__(self):
        return f'Hit {self.id}'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('hits:detail', args=[self.id])

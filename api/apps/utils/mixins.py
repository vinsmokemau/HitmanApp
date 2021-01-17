"""Django mixins utilities."""

# Django
from django.core.exceptions import PermissionDenied

# Models
from apps.users.models import User, Manager


class ManagerAccessMixin:

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.id == 1 or self.request.user.is_manager:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class BigBossAccessMixin:

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.id == 1:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

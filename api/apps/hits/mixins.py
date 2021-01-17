"""Hit mixins."""

# Django
from django.core.exceptions import PermissionDenied

# Models
from apps.hits.models import Hit


class DetailAccessMixin:

    def dispatch(self, request, *args, **kwargs):
        request_user = self.request.user
        hit = Hit.objects.get(id=kwargs['id'])

        if request_user.id == 1 or hit.creator == request_user or hit.hitman == request_user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

"""User mixins"""

# Django
from django.core.exceptions import PermissionDenied

# Models
from apps.users.models import User, Manager


class DetailAccessMixin:

    def dispatch(self, request, *args, **kwargs):
        request_user = self.request.user
        user = User.objects.get(id=kwargs['id'])

        if request_user.is_manager:
            is_lackey = user in Manager.objects.get(user=request_user).lackeys.all()
        else:
            is_lackey = False

        if user == request_user or request_user.id == 1 or is_lackey:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

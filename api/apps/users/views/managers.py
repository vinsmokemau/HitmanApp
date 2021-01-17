"""Managers views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    UpdateView,
)

# Utilities Mixins
from apps.utils.mixins import BigBossAccessMixin

# Models
from apps.users.models import User, Manager

# Forms
from apps.users.forms import AddLackeyForm


class AddLackeyView(LoginRequiredMixin, BigBossAccessMixin, UpdateView):

    model = Manager
    pk_url_kwarg = 'id'
    form_class = AddLackeyForm
    context_object_name = 'manager'
    template_name = 'managers/add_lackey.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

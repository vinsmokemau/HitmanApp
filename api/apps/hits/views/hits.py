"""Users views."""

# Django
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    FormView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    RedirectView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

# Utilities Mixins
from apps.utils.mixins import ManagerAccessMixin

# User Models
from apps.users.models import Manager

# Models
from apps.hits.models import Hit

# Forms
from apps.hits.forms import HitForm, AsigneeForm

# Mixins
from apps.hits.mixins import DetailAccessMixin


class HitList(LoginRequiredMixin, ListView):

    model = Hit
    ordering = ('-created',)
    context_object_name = 'hits'
    template_name = 'hits/list.html'

    def get_queryset(self):
        user = self.request.user
        if user.id == 1:
            return Hit.objects.all()
        elif user.is_manager:
            manager = Manager.objects.get(user=user)
            query = list(manager.lackeys.all()) + [user]
            return Hit.objects.filter(hitman__in=query)
        else:
            return Hit.objects.filter(hitman=user)


class BulkList(LoginRequiredMixin, ManagerAccessMixin, ListView):

    model = Hit
    ordering = ('-created',)
    context_object_name = 'hits'
    template_name = 'hits/list.html'

    def get_queryset(self):
        user = self.request.user
        if user.id == 1:
            return Hit.objects.filter(status='Assigned')
        elif user.is_manager:
            manager = Manager.objects.get(user=user)
            query = list(manager.lackeys.all()) + [user]
            return Hit.objects.filter(hitman__in=query, status='Assigned')


class CreateHit(LoginRequiredMixin, ManagerAccessMixin, CreateView):

    model = Hit
    form_class = HitForm
    template_name = 'hits/create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class HitDetail(LoginRequiredMixin, DetailAccessMixin, DetailView):

    model = Hit
    pk_url_kwarg = 'id'
    context_object_name = 'hit'
    template_name = 'hits/detail.html'


class FailedHit(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, **kwargs):
        hit = Hit.objects.get(id=kwargs['hit_id'])
        hit.status = 'Failed'
        hit.save()
        return hit.get_absolute_url()


class CompletedHit(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, **kwargs):
        hit = Hit.objects.get(id=kwargs['hit_id'])
        hit.status = 'Completed'
        hit.save()
        return hit.get_absolute_url()


class NewAssignee(LoginRequiredMixin, ManagerAccessMixin, UpdateView):

    model = Hit
    pk_url_kwarg = 'id'
    form_class = AsigneeForm
    context_object_name = 'hit'
    template_name = 'hits/update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

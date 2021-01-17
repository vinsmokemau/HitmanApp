"""Users views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    FormView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    RedirectView,
)

# Utilities Mixins
from apps.utils.mixins import ManagerAccessMixin

# Models
from apps.users.models import User, Manager

# Forms
from apps.users.forms import SignupForm

# Mixins
from apps.users.mixins import DetailAccessMixin


class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""

    template_name = 'users/logged_out.html'


class SignupView(FormView):
    """Users sign up view."""

    form_class = SignupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserList(LoginRequiredMixin, ManagerAccessMixin, ListView):

    model = User
    ordering = ('-created',)
    context_object_name = 'users'
    template_name = 'users/list.html'

    def get_queryset(self):
        user = self.request.user
        if user.id == 1:
            return User.objects.exclude(id=1)
        elif user.is_manager:
            manager = Manager.objects.get(user=user)
            return manager.lackeys.all()


class UserDetail(LoginRequiredMixin, DetailAccessMixin, DetailView):
    """User detail view."""

    model = User
    pk_url_kwarg = 'id'
    context_object_name = 'user'
    template_name = 'users/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.is_manager:
            manager = Manager.objects.get(user=self.object)
            context['add_lackey_url'] = reverse('users:add-lackey', args=[manager.id])
        return context


class InactiveUser(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, **kwargs):
        user = User.objects.get(id=kwargs['user_id'])
        user.is_active = False
        user.save()
        return user.get_absolute_url()

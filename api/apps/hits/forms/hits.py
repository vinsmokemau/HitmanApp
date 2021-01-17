"""Hit forms."""

# Django
from django import forms

# User Models
from apps.users.models import Manager

# Models
from apps.hits.models import Hit


class HitForm(forms.ModelForm):
    """Hit model form."""

    class Meta:
        """Form settings."""

        model = Hit
        fields = (
            'hitman',
            'target',
            'description',
        )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # restrict the queryset of 'Hitman'
        if user.is_manager:
            manager = Manager.objects.get(user=user)
            self.fields['hitman'].queryset = manager.lackeys.filter(is_active=True)
        else:
            self.fields['hitman'].queryset = self.fields['hitman'].queryset.exclude(
                id=1).filter(is_active=True)


class AsigneeForm(forms.ModelForm):
    """Hit model form."""

    class Meta:
        """Form settings."""

        model = Hit
        fields = (
            'hitman',
        )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # restrict the queryset of 'Hitman'
        if user.is_manager:
            manager = Manager.objects.get(user=user)
            self.fields['hitman'].queryset = manager.lackeys.filter(is_active=True)
        else:
            self.fields['hitman'].queryset = self.fields['hitman'].queryset.exclude(
                id=1).filter(is_active=True)

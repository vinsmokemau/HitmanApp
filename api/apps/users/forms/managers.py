"""Manager forms."""

# Django
from django import forms

# Models
from apps.users.models import User, Manager


class AddLackeyForm(forms.ModelForm):

    users = forms.ModelChoiceField(
        queryset=User.objects.exclude(
            id=1
        ).filter(
            is_active=True,
            is_manager=False,
            manager__isnull=True
        ),
        required=True,
    )

    class Meta:
        model = Manager
        fields = (
            'user',
        )
        widgets = {
            'user': forms.HiddenInput()
        }
    
    def save(self):
        data = self.cleaned_data
        user = data['user']
        manager = Manager.objects.get(user=user)
        new_lackey = data['users']
        new_lackey.manager = manager
        new_lackey.save()
        return manager

"""
class AddLackeyForm(forms.Form):
    
    users = forms.ModelChoiceField(queryset=User.objects.exclude(
        id=1).filter(is_active=True, manager__isnull=True)
    )

    def save(self):
        data = self.cleaned_data
        print(data)
"""

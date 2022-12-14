from collections import ChainMap

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from rolepermissions.roles import RolesManager

from project.account.mixins import NormalizeEmailMixin
from project.account.models import User


class UserSignupForm(NormalizeEmailMixin, UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'email',
            'password1',
            'password2',
            'role',
        )

    def __init__(self, *args, **kwargs):
        self.plain_password = User.objects.make_random_password(30)
        data = kwargs.get('data', None)
        if data is not None:
            self._set_passwords(data)
            kwargs['data'] = data
        elif args:
            query_dict = args[0]
            dct = {}
            self._set_passwords(dct)
            args = (ChainMap(query_dict, dct), *args[1:])
        super().__init__(*args, **kwargs)
        self._normalize_email()

    def _set_passwords(self, data):
        if 'password1' not in data and 'password2' not in data:
            data['password1'] = data['password2'] = self.plain_password

    password1 = forms.CharField(
        label=_('Password'),
        strip=False,
        required=True,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput,
        strip=False,
        required=True,
        help_text=_('Enter the same password as before, for verification.'),
    )
    role = forms.ChoiceField(
        label=_('Category'),
        choices=[(role, role) for role in RolesManager.get_roles_names()],
    )

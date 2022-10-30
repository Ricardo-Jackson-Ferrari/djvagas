from django.db import transaction
from rolepermissions.roles import RolesManager as _RolesManager
from rolepermissions.roles import get_user_roles as _get_user_roles

from project.roles import Candidate as _Candidate

from .models import ProfileCandidate as _ProfileCandidate

__all__ = [
    'create_candidate',
    'create_company',
]


class UserIsNotCandidate(Exception):
    pass


def _create_candidate_profile(user):
    if _Candidate in _get_user_roles(user):
        _ProfileCandidate.objects.create(candidate=user)
    else:
        raise UserIsNotCandidate()


def _user_assign_role(user, role):
    _RolesManager.retrieve_role(role).assign_role_to_user(user)


def _create_user(form):
    user = form.save()

    _user_assign_role(user, form.cleaned_data['role'])

    return user


@transaction.atomic
def create_candidate(form):
    user = _create_user(form)

    _create_candidate_profile(user)

    return user


def create_company(form):
    user = _create_user(form)

    return user

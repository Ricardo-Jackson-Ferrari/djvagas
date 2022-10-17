from rolepermissions.roles import RolesManager as _RolesManager
from rolepermissions.roles import get_user_roles as _get_user_roles

from project.roles import Candidate as _Candidate

from .models import ProfileCandidate as _ProfileCandidate

__all__ = [
    'create_candidate_profile',
    'user_assign_role',
    'UserIsNotCandidate',
]


class UserIsNotCandidate(Exception):
    pass


def create_candidate_profile(user):
    if _Candidate in _get_user_roles(user):
        _ProfileCandidate.objects.create(candidate=user)
    else:
        raise UserIsNotCandidate()


def user_assign_role(user, role):
    _RolesManager.retrieve_role(role).assign_role_to_user(user)

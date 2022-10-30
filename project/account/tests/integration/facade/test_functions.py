from django.contrib.auth import get_user_model
from django.test import TestCase
from model_bakery import baker
from rolepermissions.roles import assign_role, get_user_roles

from project.account import facade
from project.account.models import ProfileCandidate
from project.roles import Candidate


class FacadeIntegrationTest(TestCase):
    def test_create_candidate_profile_success(self):
        user = baker.make(get_user_model())
        assign_role(user, Candidate.get_name())

        facade._create_candidate_profile(user)

        self.assertTrue(ProfileCandidate.objects.get(candidate=user))

    def test_create_candidate_profile_error(self):
        user = baker.make(get_user_model())

        self.assertRaises(
            facade.UserIsNotCandidate,
            facade._create_candidate_profile,
            user=user,
        )

    def test_user_assign_role(self):
        user = baker.make(get_user_model())
        role = Candidate
        facade._user_assign_role(user, role.get_name())

        self.assertTrue(role in get_user_roles(user))

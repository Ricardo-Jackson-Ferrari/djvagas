from django.test import TestCase
from model_bakery import baker
from pytest import mark


@mark.unit
class ProfileCandidateUnittest(TestCase):
    def test_return_str(self):
        schooling = baker.make('Schooling')
        profile = baker.make('ProfileCandidate', schooling=schooling)
        self.assertEqual(profile.candidate.first_name, str(profile))

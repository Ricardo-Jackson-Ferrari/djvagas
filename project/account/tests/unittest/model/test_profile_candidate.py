from django.test import SimpleTestCase
from model_bakery import baker
from pytest import mark


@mark.unit
class ProfileCandidateUnittest(SimpleTestCase):
    def test_return_str(self):
        schooling = baker.prepare('Schooling')
        profile = baker.prepare('ProfileCandidate', schooling=schooling)
        self.assertEqual(profile.candidate.first_name, str(profile))

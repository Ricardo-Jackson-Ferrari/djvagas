from django.test import SimpleTestCase
from django.utils.translation import gettext_lazy as _
from model_bakery import baker
from parameterized import parameterized
from pytest import mark

from project.job.models import Application


@mark.unit
class ApplicationUnittest(SimpleTestCase):
    @parameterized.expand(
        [
            (0, 1, 500, 100),
            (1, 0, 500, 50),
        ]
    )
    def test_return_correct_score(
        self,
        job_schooling_level,
        candidate_schooling_level,
        candidate_salary_expectation,
        score_expectation,
    ):
        job_schooling = baker.prepare('Schooling', level=job_schooling_level)
        candidate_schooling = baker.prepare(
            'Schooling', level=candidate_schooling_level
        )

        job_salary_from = 1000
        job_salary_to = 2000

        job = baker.prepare(
            'Job',
            salary_from=job_salary_from,
            salary_to=job_salary_to,
            schooling=job_schooling,
        )

        job_application = baker.prepare(
            Application,
            job=job,
            salary_expectation=candidate_salary_expectation,
        )

        baker.prepare(
            'ProfileCandidate',
            candidate=job_application.candidate,
            schooling=candidate_schooling,
        )

        self.assertEqual(job_application.calculate_score(), score_expectation)

    def test_return_str(self):
        job_application = baker.prepare(Application)
        self.assertEqual(job_application.job.title, str(job_application))

    @parameterized.expand(
        [
            (
                _('%(model_name)s with this %(field_labels)s already exists.'),
                ('status', 'job'),
            ),
            (
                _('%(candidate)s already registered for job.'),
                ('candidate', 'job'),
            ),
        ]
    )
    def test_unique_error_message(self, msg, unique_check):
        job_application = baker.prepare(Application)
        error = job_application.unique_error_message(
            model_class=Application, unique_check=unique_check
        )
        self.assertEqual(msg, error.message)

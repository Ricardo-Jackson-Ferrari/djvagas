from project.job.forms import JobCreateForm as _JobCreateForm

from .models import Application as _Application
from .models import Job as _Job

__all__ = [
    'JobDoesNotExist',
    'get_full_job_list',
    'get_authorized_job_list',
    'get_activated_authorized_job_list',
    'get_user_job_list',
    'get_user_application_list',
    'get_user_candidate',
]
JobDoesNotExist = _Job.DoesNotExist


def get_full_job_list():
    return _Job.objects.all()


def get_authorized_job_list():
    return _Job.objects.filter(checked=True)


def get_activated_authorized_job_list():
    return get_authorized_job_list().filter(status=True)


def get_user_job_list(user):
    return get_full_job_list().filter(company=user)


def get_user_application_list(user):
    return _Application.objects.filter(candidate=user)


def get_job_activated_authorized_with_slug(slug):
    return _Job.objects.filter(status=True, checked=True).get(slug=slug)

from project.job.forms import JobCreateForm as _JobCreateForm

from .models import Job as _Job

__all__ = [
    'get_full_job_list',
    'get_full_authorized_job_list',
    'get_activated_authorized_job_list',
    'get_user_job_list',
    'get_job_create_form',
]


def get_full_job_list():
    return _Job.objects.all()


def get_full_authorized_job_list():
    return _Job.objects.filter(checked=True)


def get_activated_authorized_job_list():
    return get_full_authorized_job_list().filter(status=True)


def get_user_job_list(user):
    return get_full_job_list().filter(company=user)


def get_job_create_form():
    return _JobCreateForm

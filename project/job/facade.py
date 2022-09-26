from .models import Job


def job_list():
    return Job.objects.filter(status=True)
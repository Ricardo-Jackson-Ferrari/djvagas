from .models import Job


def get_job_list():
    return Job.objects.filter(status=True)

from django.core.management.base import BaseCommand
from project.job.models import Job
from model_bakery import baker
from django.utils.text import slugify
from faker import Faker
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'job_create_data'

    def create_jobs(self, qtd=10):
        aux_list = []
        for _ in range(qtd):
            obj = Job(**self.get_job())
            aux_list.append(obj)
        Job.objects.bulk_create(aux_list)

    def get_job(self):
        faker = Faker()
        data = {
            'schooling': baker.make('Schooling'),
            'company': baker.make(get_user_model()),
            'salary_range': baker.make('Salary'),
            'title': faker.text(),
            'description': faker.text(),
            'status': faker.boolean(),
            'slug': slugify(faker.name()),
        }

        return data

    def handle(self, *args, **options):
        self.create_jobs()
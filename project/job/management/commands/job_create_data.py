from random import randint

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
from model_bakery import baker
from rolepermissions.roles import assign_role

from project.job.models import Job
from project.roles import Company


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
        salary = randint(500, 5000)
        company = baker.make(get_user_model())
        assign_role(company, Company.get_name())
        data = {
            'schooling': baker.make('Schooling'),
            'company': company,
            'salary_from': salary,
            'salary_to': salary + 100,
            'title': faker.text(),
            'description': faker.text(),
            'status': faker.boolean(),
            'checked': faker.boolean(),
            'slug': slugify(faker.name()),
        }

        return data

    def handle(self, *args, **options):
        self.create_jobs()

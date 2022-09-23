# Generated by Django 4.1.1 on 2022-09-23 04:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'salary_range',
                    models.CharField(
                        max_length=30, unique=True, verbose_name='salary range'
                    ),
                ),
            ],
            options={
                'verbose_name': 'salary',
            },
        ),
        migrations.CreateModel(
            name='Schooling',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'schooling',
                    models.CharField(
                        max_length=30, unique=True, verbose_name='schooling'
                    ),
                ),
                ('level', models.PositiveIntegerField(verbose_name='level')),
            ],
            options={
                'verbose_name': 'schooling',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='created at'
                    ),
                ),
                (
                    'updated_on',
                    models.DateTimeField(
                        auto_now=True, verbose_name='updated on'
                    ),
                ),
                (
                    'title',
                    models.CharField(max_length=100, verbose_name='title'),
                ),
                ('status', models.BooleanField(default=False)),
                (
                    'description',
                    models.TextField(
                        max_length=500, verbose_name='description'
                    ),
                ),
                (
                    'company',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='company',
                    ),
                ),
                (
                    'salary_range',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to='job.salary',
                        verbose_name='salary range',
                    ),
                ),
                (
                    'schooling',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to='job.schooling',
                        verbose_name='schooling',
                    ),
                ),
            ],
            options={
                'verbose_name': 'job',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='created at'
                    ),
                ),
                (
                    'updated_on',
                    models.DateTimeField(
                        auto_now=True, verbose_name='updated on'
                    ),
                ),
                ('status', models.BooleanField(default=True)),
                ('experience', models.TextField(verbose_name='experience')),
                (
                    'attending',
                    models.BooleanField(
                        default=False, verbose_name='attending'
                    ),
                ),
                ('objective', models.TextField(verbose_name='objective')),
                (
                    'candidate',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='candidate',
                    ),
                ),
                (
                    'job',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='job.job',
                        verbose_name='job',
                    ),
                ),
                (
                    'salary_expectation',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='job.salary',
                        verbose_name='salary expectation',
                    ),
                ),
                (
                    'schooling',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to='job.schooling',
                        verbose_name='schooling',
                    ),
                ),
            ],
            options={
                'verbose_name': 'application',
                'unique_together': {('candidate', 'job')},
            },
        ),
    ]

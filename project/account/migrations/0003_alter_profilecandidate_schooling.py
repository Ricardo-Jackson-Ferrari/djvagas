# Generated by Django 4.1.1 on 2022-10-14 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
        ('account', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilecandidate',
            name='schooling',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='job.schooling',
                verbose_name='schooling',
            ),
        ),
    ]

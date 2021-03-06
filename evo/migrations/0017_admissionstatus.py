# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-12 05:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evo', '0016_studentcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic', models.BooleanField(default=False)),
                ('address', models.BooleanField(default=False)),
                ('qualifications', models.BooleanField(default=False)),
                ('uploads', models.BooleanField(default=False)),
                ('terms', models.BooleanField(default=False)),
                ('finalsubmission', models.BooleanField(default=False)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

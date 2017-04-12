# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-12 06:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evo', '0017_admissionstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusstudent',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

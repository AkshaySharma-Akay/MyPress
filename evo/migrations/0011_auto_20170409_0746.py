# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-09 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evo', '0010_auto_20170409_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='semester_count',
            field=models.PositiveSmallIntegerField(unique=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-09 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evo', '0013_auto_20170409_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusstudent',
            name='admission',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='statusstudent',
            name='profile',
            field=models.BooleanField(default=False),
        ),
    ]
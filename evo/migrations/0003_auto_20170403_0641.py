# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-03 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evo', '0002_auto_20170403_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='years',
            field=models.PositiveSmallIntegerField(),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-03 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evo', '0003_auto_20170403_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_id',
            field=models.CharField(default='vca', max_length=25, unique=False),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-17 05:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evo', '0027_auto_20170417_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evoarticle',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-19 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woark', '0006_auto_20170317_0716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='woark.ArticleTag'),
        ),
    ]

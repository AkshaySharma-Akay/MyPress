# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-10 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('link', models.URLField(default=b'https://localhost')),
            ],
        ),
        migrations.CreateModel(
            name='SiteContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('info', models.CharField(max_length=30)),
                ('icon', models.CharField(max_length=15)),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteSocialProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('icon', models.CharField(max_length=15)),
                ('link', models.URLField()),
            ],
        ),
    ]

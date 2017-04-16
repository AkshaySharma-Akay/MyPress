# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-13 08:04
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evo', '0020_auto_20170412_0655'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentQualifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[[b'1', b'10Th'], [b'10+2', b'10+2']], max_length=3)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1970), django.core.validators.MaxValueValidator(2015)])),
                ('board', models.CharField(max_length=150)),
                ('institute', models.CharField(max_length=150)),
                ('percentage', models.IntegerField(validators=[django.core.validators.MinValueValidator(33), django.core.validators.MaxValueValidator(100)])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-17 05:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evo', '0026_auto_20170417_0453'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvoArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(max_length=7000)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EvoArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='studentuploads',
            name='plustwo',
            field=models.ImageField(max_length=120, upload_to=b'stu_doc/', verbose_name=b'10+2 Details Marks'),
        ),
        migrations.AlterField(
            model_name='studentuploads',
            name='signature',
            field=models.ImageField(max_length=120, upload_to=b'stu_images/', verbose_name=b'Signature'),
        ),
        migrations.AlterField(
            model_name='studentuploads',
            name='stu_image',
            field=models.ImageField(max_length=120, upload_to=b'stu_images/', verbose_name=b'Student Image'),
        ),
        migrations.AlterField(
            model_name='studentuploads',
            name='tenth',
            field=models.ImageField(max_length=120, upload_to=b'stu_doc/', verbose_name=b'Tenth Details Marks'),
        ),
        migrations.AddField(
            model_name='evoarticle',
            name='tag',
            field=models.ManyToManyField(to='evo.EvoArticleTag'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-17 07:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('woark', '0005_auto_20170317_0651'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plain_content', models.TextField(max_length=5000)),
                ('markup_content', models.TextField(max_length=7000)),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=700),
        ),
        migrations.AddField(
            model_name='articlecontent',
            name='article',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='woark.Article'),
        ),
    ]
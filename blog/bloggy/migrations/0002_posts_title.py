# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='title',
            field=models.CharField(default='My Post Title', max_length=30),
        ),
    ]
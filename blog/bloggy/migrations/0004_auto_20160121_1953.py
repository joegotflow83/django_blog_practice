# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 19:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggy', '0003_auto_20160121_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-02 21:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191003_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 10, 2, 21, 2, 9, 444724, tzinfo=utc)),
        ),
    ]
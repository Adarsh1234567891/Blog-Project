# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-02 21:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191003_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
    ]

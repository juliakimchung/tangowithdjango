# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20170122_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-07-06 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='my location default', max_length=120),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-28 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20170125_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_address',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]

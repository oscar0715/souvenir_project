# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 14:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20170112_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='card_sent',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20170112_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='card_left',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='card_sent',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_quantity',
            field=models.PositiveIntegerField(),
        ),
    ]

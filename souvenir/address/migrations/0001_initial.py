# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User_Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.IntegerField()),
                ('province', models.IntegerField()),
                ('city', models.IntegerField()),
                ('district', models.IntegerField()),
                ('detail_address', models.CharField(max_length=200)),
                ('postcode', models.PositiveIntegerField()),
                ('receiver_name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.MyProfile')),
            ],
        ),
    ]

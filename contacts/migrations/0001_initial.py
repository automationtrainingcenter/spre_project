# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-02-05 12:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('listing', models.IntegerField()),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=5000)),
                ('contact_date', models.DateField(default=datetime.datetime(2020, 2, 5, 17, 57, 29, 821546))),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-02-05 12:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]

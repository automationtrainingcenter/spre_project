# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-23 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo_1',
            field=models.ImageField(default='', upload_to='media/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_2',
            field=models.ImageField(default='', upload_to='media/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_3',
            field=models.ImageField(default='', upload_to='media/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_4',
            field=models.ImageField(default='', upload_to='media/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_5',
            field=models.ImageField(default='', upload_to='media/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_6',
            field=models.ImageField(default='', upload_to='media/%y/%m/%d'),
        ),
    ]

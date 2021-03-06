# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-23 12:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('garage', models.IntegerField(default=0)),
                ('sqft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=5)),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateField(default=datetime.datetime.today)),
                ('photo_main', models.ImageField(upload_to='media/%y/%m/%d')),
                ('photo_1', models.ImageField(upload_to='media/%y/%m/%d')),
                ('photo_2', models.ImageField(upload_to='media/%y/%m/%d')),
                ('photo_3', models.ImageField(upload_to='media/%y/%m/%d')),
                ('photo_4', models.ImageField(upload_to='media/%y/%m/%d')),
                ('photo_5', models.ImageField(upload_to='media/%y/%m/%d')),
                ('photo_6', models.ImageField(upload_to='media/%y/%m/%d')),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor')),
            ],
        ),
    ]

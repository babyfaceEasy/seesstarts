# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-28 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BioData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
    ]
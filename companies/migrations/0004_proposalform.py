# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-01 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposalForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('plans', models.ManyToManyField(to='companies.Plan')),
            ],
        ),
    ]

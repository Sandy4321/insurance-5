# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-01 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_proposalform'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposalFormBooleanField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('required', models.BooleanField(default=True)),
                ('value', models.BooleanField()),
                ('proposal_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.ProposalForm')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProposalFormFileField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('required', models.BooleanField(default=True)),
                ('value', models.FileField(upload_to=b'')),
                ('proposal_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.ProposalForm')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProposalFormNumberField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('required', models.BooleanField(default=True)),
                ('value', models.FloatField()),
                ('proposal_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.ProposalForm')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProposalFormTextField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('required', models.BooleanField(default=True)),
                ('value', models.CharField(max_length=255)),
                ('proposal_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.ProposalForm')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

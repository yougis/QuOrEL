# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 15:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0005_auto_20160111_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sequence',
            name='mension',
        ),
        migrations.AddField(
            model_name='mension',
            name='Sequence',
            field=models.ManyToManyField(to='inventaire.Sequence'),
        ),
        migrations.AlterField(
            model_name='document',
            name='annee',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2016)]),
        ),
        migrations.AlterField(
            model_name='operation',
            name='nom_operation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='nom_sequence',
            field=models.CharField(max_length=100),
        ),
    ]

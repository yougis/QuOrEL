# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 17:34
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0005_auto_20160129_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, dim=3, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='sondage',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, dim=3, null=True, srid=4326),
        ),
    ]

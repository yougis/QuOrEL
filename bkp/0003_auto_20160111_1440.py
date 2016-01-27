# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0002_auto_20160111_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unite',
            name='tache',
        ),
        migrations.AddField(
            model_name='mension',
            name='document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventaire.Document'),
        ),
        migrations.AddField(
            model_name='observation',
            name='sequence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventaire.Sequence'),
        ),
        migrations.AddField(
            model_name='observation',
            name='sondage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventaire.Sondage'),
        ),
        migrations.AddField(
            model_name='sequence',
            name='mension',
            field=models.ManyToManyField(blank=True, null=True, to='inventaire.Mension'),
        ),
        migrations.AddField(
            model_name='sondage',
            name='operation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventaire.Operation'),
        ),
        migrations.AddField(
            model_name='unite',
            name='sequence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventaire.Sequence'),
        ),
        migrations.AddField(
            model_name='unite',
            name='taches',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='nom_document',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='observation',
            name='nom_observation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sondage',
            name='nom_sondage',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='unite',
            name='nom_unite',
            field=models.CharField(max_length=100),
        ),
    ]
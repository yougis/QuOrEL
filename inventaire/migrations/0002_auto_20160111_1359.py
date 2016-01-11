# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='type_obs',
            field=models.CharField(choices=[('log', 'log'), ('coupe', 'coupe'), ('plan', 'plan')], default='indéfini', max_length=5),
        ),
        migrations.AddField(
            model_name='operation',
            name='type_op',
            field=models.CharField(choices=[('fouille préventive', 'fouille préventive'), ('diagnostic préventif', 'diagnostic préventif'), ('fouille programmée', 'fouille programmée'), ('carrière', 'carrière'), ('autre chantier', 'autre chantier'), ('autre', 'autre')], default='indéfini', max_length=25),
        ),
        migrations.AddField(
            model_name='unite',
            name='couleur',
            field=models.CharField(choices=[('blanc', 'blanc'), ('noir', 'noir'), ('brun', 'brun'), ('jaune', 'jaune'), ('orange', 'orange'), ('rouge', 'rouge'), ('vert', 'vert'), ('bleu', 'bleu'), ('rouille', 'rouille'), ('clair', 'clair')], default='indéfini', max_length=2),
        ),
        migrations.AddField(
            model_name='unite',
            name='structure',
            field=models.CharField(choices=[('massive', 'massive'), ('lamellaire', 'lamellaire'), ('polyyédrique', 'polyyédrique'), ('prismatique', 'prismatique'), ('grossière', 'grossière'), ('fine', 'fine')], default='indéfini', max_length=2),
        ),
        migrations.AddField(
            model_name='unite',
            name='texture',
            field=models.CharField(choices=[('caillouteux', 'caillouteux'), ('graveleux', 'graveleux'), ('sableux', 'sableux'), ('limoneux', 'limoneux'), ('argileux', 'argileux')], default='indéfini', max_length=2),
        ),
    ]
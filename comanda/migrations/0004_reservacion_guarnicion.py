# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0002_auto_20160921_1745'),
        ('comanda', '0003_auto_20160921_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservacion',
            name='guarnicion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_guarnicion', to='configuracion.Alimento'),
        ),
    ]

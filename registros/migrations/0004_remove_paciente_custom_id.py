# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-16 02:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0003_auto_20161115_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='custom_id',
        ),
    ]

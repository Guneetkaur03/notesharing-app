# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-27 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20180227_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details_notes',
            name='subject',
            field=models.CharField(max_length=200),
        ),
    ]
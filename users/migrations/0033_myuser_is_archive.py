# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-07 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_auto_20170602_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_archive',
            field=models.BooleanField(default=False, verbose_name='Архив'),
        ),
    ]

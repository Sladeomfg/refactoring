# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 07:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stantions', '0004_auto_20170222_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stantion',
            name='user',
        ),
        migrations.AddField(
            model_name='stantion',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Агент'),
        ),
    ]

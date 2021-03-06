# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stantions', '0017_auto_20170401_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='interface',
            field=models.CharField(blank=True, choices=[('eaisto', 'ЕАИСТО'), ('eaisto_online', 'eaisto.online'), ('to95', 'to95.net')], default='eaisto', max_length=255, verbose_name='Интерфейс'),
        ),
        migrations.AlterField(
            model_name='stantion',
            name='interface',
            field=models.CharField(blank=True, choices=[('eaisto', 'ЕАИСТО'), ('eaisto_online', 'eaisto.online'), ('to95', 'to95.net')], default='eaisto', max_length=255, verbose_name='Интерфейс'),
        ),
    ]

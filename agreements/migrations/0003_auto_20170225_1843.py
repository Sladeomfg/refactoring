# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreements', '0002_auto_20170223_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='pts_num',
            field=models.CharField(max_length=6, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='pts_serial',
            field=models.CharField(max_length=4, verbose_name='Серия'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='srts_num',
            field=models.CharField(max_length=6, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='srts_serial',
            field=models.CharField(max_length=4, verbose_name='Серия'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-04 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stantions', '0020_auto_20170602_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generator',
            name='is_enable_for_all',
            field=models.BooleanField(default=False, verbose_name='Включить генератор для всех'),
        ),
        migrations.AlterField(
            model_name='generatoroperatornum',
            name='reg_number',
            field=models.IntegerField(help_text='Регистрационный номер в реестре операторов, состоящий из пяти символов.', max_length=255, verbose_name='Рег. номер'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20170204_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='ts_sub_category',
            field=models.IntegerField(blank=True, verbose_name='Подкатегория ТС'),
        ),
    ]
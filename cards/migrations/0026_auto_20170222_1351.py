# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0025_request_user_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='ts_vin',
            field=models.CharField(blank=True, help_text='Если отсутствует, то не заполняется', max_length=255, verbose_name='VIN'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0017_auto_20170220_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='notes',
            field=models.CharField(blank=True, max_length=255, verbose_name='Примечание'),
        ),
    ]

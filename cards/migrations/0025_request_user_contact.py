# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0024_auto_20170222_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='user_contact',
            field=models.CharField(blank=True, max_length=255, verbose_name='Телефон или email'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0031_requestautogennumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='is_foreign',
            field=models.BooleanField(default=False, verbose_name='Иностранный гражданин'),
        ),
    ]

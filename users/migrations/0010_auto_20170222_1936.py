# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20170220_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='email_confirm_key',
            field=models.UUIDField(blank=True, editable=False, null=True, verbose_name='Ключ подтверждения почты'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_email_confirm',
            field=models.BooleanField(default=False, verbose_name='Почта подтверждена'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 11:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stantions', '0007_auto_20170223_1543'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stantion',
            options={'ordering': ('order', 'id'), 'permissions': (('can_change_self', 'Может изменять свои станции'),)},
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20170326_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='stantion_order_type',
            field=models.IntegerField(blank=True, choices=[(1, 'Равномерно'), (2, 'По очереди')], default=1, help_text='Распостраняется только на тех, у кого есть свои станции.', verbose_name='Тип очереди для станций'),
        ),
    ]

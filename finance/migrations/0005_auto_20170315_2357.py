# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_auto_20170301_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.IntegerField(choices=[(1, 'Создана'), (2, 'В процессе'), (3, 'Исполнена'), (4, 'Отменена')], default=1, verbose_name='Статус'),
        ),
    ]
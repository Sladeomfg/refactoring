# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.IntegerField(choices=[(1, 'Создана'), (2, 'Ожидает отправки'), (3, 'В процессе'), (4, 'Выполнена'), (5, 'Отменена')], default=1, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='request',
            name='ts_mileage',
            field=models.IntegerField(blank=True, verbose_name='Пробег'),
        ),
    ]

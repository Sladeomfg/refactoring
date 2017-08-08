# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0014_request_reg_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='ts_category',
            field=models.IntegerField(choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'Прицеп')], verbose_name='Категория ТС'),
        ),
        migrations.AlterField(
            model_name='request',
            name='ts_sub_category',
            field=models.IntegerField(blank=True, choices=[(1, 'M1 (легковые до 8-ми пассажирских мест)'), (2, 'N1 (грузовые с максимальной массой не более 3,5 тонн)')], null=True, verbose_name='Подкатегория ТС'),
        ),
    ]

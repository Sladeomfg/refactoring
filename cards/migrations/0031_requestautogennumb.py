# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0030_auto_20170310_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestAutoGenNumb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stantion_num', models.IntegerField(verbose_name='Рег номер пункта ТО')),
                ('expert_id', models.IntegerField(verbose_name='Номер эксперта')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('card_num', models.IntegerField(verbose_name='Номер карты')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
    ]

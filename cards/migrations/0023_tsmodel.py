# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 10:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0022_auto_20170222_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='TsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.TsMark')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]

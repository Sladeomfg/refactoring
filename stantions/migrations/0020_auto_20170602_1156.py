# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-02 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stantions', '0019_auto_20170427_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_enable_for_all', models.BooleanField(default=False, verbose_name='Включено для всех')),
            ],
        ),
        migrations.CreateModel(
            name='GeneratorOperatorNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(help_text='Регистрационный номер в реестре операторов, состоящий из пяти символов.', max_length=255, verbose_name='Рег. номер')),
            ],
        ),
        migrations.AddField(
            model_name='generator',
            name='reg_nums',
            field=models.ManyToManyField(to='stantions.GeneratorOperatorNum'),
        ),
    ]

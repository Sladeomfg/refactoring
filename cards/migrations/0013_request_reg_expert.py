# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 18:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stantions', '0002_auto_20170209_2120'),
        ('cards', '0012_request_expire_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='reg_expert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stantions.Expert'),
        ),
    ]
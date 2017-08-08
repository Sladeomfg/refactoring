# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 11:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_userprintsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_test_access',
            field=models.BooleanField(default=False, verbose_name='Тестовый доступ'),
        ),
        migrations.AlterField(
            model_name='userprintsettings',
            name='stamp',
            field=models.ImageField(blank=True, null=True, upload_to='stamp/', verbose_name='Печать'),
        ),
        migrations.AlterField(
            model_name='userprintsettings',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='print_settings', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 07:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('is_read', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('level', models.IntegerField(choices=[(1, 'Зеленый'), (2, 'Синий'), (3, 'Жёлтый'), (4, 'Красный')], default=2, verbose_name='Тип')),
                ('date_send', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_sent', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_received', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-20 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20180620_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
        migrations.AddField(
            model_name='book',
            name='short_desc',
            field=models.TextField(blank=True, max_length=100, verbose_name='краткое описание'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-20 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20180620_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=150, verbose_name='имя книги'),
        ),
    ]

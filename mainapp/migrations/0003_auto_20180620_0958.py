# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-20 06:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20180620_0946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-surname']},
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-16 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20180415_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='url',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
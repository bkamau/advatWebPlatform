# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advat', '0009_auto_20160229_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='sale_description',
            field=models.TextField(max_length=5000),
        ),
    ]

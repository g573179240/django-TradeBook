# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-23 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='views',
            field=models.IntegerField(default=0, verbose_name='浏览数量'),
        ),
    ]
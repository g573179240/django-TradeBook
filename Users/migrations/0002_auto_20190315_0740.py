# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-15 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='password',
            field=models.CharField(max_length=50, verbose_name='用户密码'),
        ),
    ]
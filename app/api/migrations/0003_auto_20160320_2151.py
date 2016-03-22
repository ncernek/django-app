# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 03:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160320_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_password_update',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_update',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

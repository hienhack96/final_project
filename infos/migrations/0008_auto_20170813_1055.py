# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0007_auto_20170813_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='notify',
            name='noti_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='notify',
            name='noti_type',
            field=models.CharField(blank=True, choices=[('1', 'like'), ('2', 'comment'), ('3', 'rating')], max_length=10, null=True),
        ),
    ]

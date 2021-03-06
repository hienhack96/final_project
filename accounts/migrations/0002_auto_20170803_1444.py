# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 07:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='votes',
        ),
        migrations.AddField(
            model_name='user',
            name='rater',
            field=models.ManyToManyField(blank=True, related_name='_user_rater_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]

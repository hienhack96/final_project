# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 01:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('infos', '0002_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='bevoted_username',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='vote_username',
        ),
        migrations.AddField(
            model_name='rating',
            name='from_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rating',
            name='to_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
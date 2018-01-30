# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-29 07:19
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0007_auto_20180120_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deletedvideo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='deletedvideo',
            name='name',
        ),
        migrations.RemoveField(
            model_name='deletedvideo',
            name='original_pk',
        ),
        migrations.RemoveField(
            model_name='deletedvideo',
            name='uploader',
        ),
        migrations.RemoveField(
            model_name='deletedvideo',
            name='url',
        ),
        migrations.AddField(
            model_name='deletedvideo',
            name='video_uuid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='dvapql',
            name='error_message',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='dvapql',
            name='failed',
            field=models.BooleanField(default=False),
        ),
    ]
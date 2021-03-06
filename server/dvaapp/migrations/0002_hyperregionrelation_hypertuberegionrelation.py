# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-10 09:41
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0001_auto_20180608_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='HyperRegionRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('weight', models.FloatField(null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('path', models.TextField()),
                ('full_frame', models.BooleanField(default=False)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('h', models.IntegerField(default=0)),
                ('w', models.IntegerField(default=0)),
                ('frame_index', models.IntegerField(null=True)),
                ('segment_index', models.IntegerField(null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Region')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video')),
            ],
        ),
        migrations.CreateModel(
            name='HyperTubeRegionRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('weight', models.FloatField(null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('path', models.TextField()),
                ('full_frame', models.BooleanField(default=False)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('h', models.IntegerField(default=0)),
                ('w', models.IntegerField(default=0)),
                ('frame_index', models.IntegerField(null=True)),
                ('segment_index', models.IntegerField(null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent')),
                ('tube', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Tube')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video')),
            ],
        ),
    ]

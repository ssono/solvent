# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 03:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_auto_20171105_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ideas.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ideas.Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='mods',
            field=models.ManyToManyField(to='ideas.Profile'),
        ),
    ]

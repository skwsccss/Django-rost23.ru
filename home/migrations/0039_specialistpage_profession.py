# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-25 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_specialistpage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialistpage',
            name='profession',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Профессия'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-16 08:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_contactpage_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactpage',
            name='text',
        ),
    ]
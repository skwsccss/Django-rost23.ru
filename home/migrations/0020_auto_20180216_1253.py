# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-16 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20180216_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricepage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image'),
        ),
    ]
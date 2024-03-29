# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-19 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0034_testimonialimage'),
        ('service', '0004_auto_20180219_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('text', wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='Текст')),
                ('categories', modelcluster.fields.ParentalManyToManyField(blank=True, related_name='category_in_service', to='home.CategoryPrice', verbose_name='Категории цен')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-02 15:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finderApp', '0005_recipe_creater'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='creater',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-25 08:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20190125_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='deviceTpye',
            new_name='deviceType',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='pthoto_url',
            new_name='photo_url',
        ),
    ]
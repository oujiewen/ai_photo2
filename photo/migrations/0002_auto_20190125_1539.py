# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-25 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='car_groupId',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='photo',
            name='deviceTpye',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='photo',
            name='status',
            field=models.IntegerField(),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0003_auto_20160405_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]

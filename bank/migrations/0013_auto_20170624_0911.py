# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0012_auto_20170624_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='branch_image',
            field=models.FileField(blank=True, default=False, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='subject',
            name='question_image',
            field=models.FileField(blank=True, default=False, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_image',
            field=models.FileField(blank=True, default=False, upload_to=b''),
        ),
    ]

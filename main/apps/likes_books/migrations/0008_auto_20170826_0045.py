# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-26 00:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes_books', '0007_auto_20170826_0036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='uploader',
            new_name='uploaded_by',
        ),
    ]

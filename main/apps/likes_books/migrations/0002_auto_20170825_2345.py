# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-25 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes_books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='liked_users',
        ),
        migrations.AddField(
            model_name='like',
            name='liked_books',
            field=models.ManyToManyField(related_name='books', to='likes_books.Book'),
        ),
        migrations.AddField(
            model_name='like',
            name='liked_users',
            field=models.ManyToManyField(related_name='users', to='likes_books.User'),
        ),
    ]

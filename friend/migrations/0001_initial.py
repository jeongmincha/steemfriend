# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('friend_update_date', models.DateTimeField(verbose_name='date when friend list is updated ')),
                ('friend_list', models.CharField(max_length=1000)),
            ],
        ),
    ]

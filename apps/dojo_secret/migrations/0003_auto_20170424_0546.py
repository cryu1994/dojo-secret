# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-24 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_secret', '0002_auto_20170424_0333'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='CommentManager',
        ),
    ]
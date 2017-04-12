# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-10 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20170409_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=453)),
            ],
        ),
        migrations.RenameField(
            model_name='bookdetails',
            old_name='category',
            new_name='subtitle',
        ),
        migrations.AddField(
            model_name='bookdetails',
            name='categories',
            field=models.ManyToManyField(to='books.Category'),
        ),
    ]
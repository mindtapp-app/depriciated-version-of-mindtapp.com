# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-23 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20170923_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='WordList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.WordList'),
        ),
    ]
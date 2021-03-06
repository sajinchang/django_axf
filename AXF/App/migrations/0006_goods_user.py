# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-16 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20181216_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=16)),
                ('productimg', models.CharField(max_length=128)),
                ('productname', models.CharField(max_length=64)),
                ('productlongname', models.CharField(max_length=128)),
                ('isxf', models.IntegerField(default=0)),
                ('pmdesc', models.IntegerField(default=0)),
                ('specifics', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('marketprice', models.FloatField()),
                ('categoryid', models.IntegerField()),
                ('childcid', models.IntegerField()),
                ('childcidname', models.CharField(max_length=64)),
                ('dealerid', models.CharField(max_length=32)),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('nickname', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=128)),
                ('img', models.ImageField(upload_to='%Y/%m/%d/%H/%M/%S/icons')),
                ('level', models.IntegerField(default=1)),
                ('token', models.CharField(max_length=256)),
                ('active', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=True)),
                ('email', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]

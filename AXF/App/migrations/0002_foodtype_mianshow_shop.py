# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-13 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=16)),
                ('typename', models.CharField(max_length=32)),
                ('childtypenames', models.CharField(max_length=256)),
                ('typesort', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MianShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=64)),
                ('trackid', models.CharField(max_length=16)),
                ('categoryid', models.CharField(max_length=16)),
                ('brandname', models.CharField(max_length=32)),
                ('img1', models.CharField(max_length=255)),
                ('childcid1', models.CharField(max_length=16)),
                ('productid1', models.CharField(max_length=16)),
                ('logname1', models.CharField(max_length=128)),
                ('price1', models.CharField(max_length=16)),
                ('marketprice1', models.CharField(max_length=16)),
                ('img2', models.CharField(max_length=255)),
                ('childcid2', models.CharField(max_length=26)),
                ('productid2', models.CharField(max_length=26)),
                ('logname2', models.CharField(max_length=228)),
                ('price2', models.CharField(max_length=26)),
                ('marketprice2', models.CharField(max_length=26)),
                ('img3', models.CharField(max_length=255)),
                ('childcid3', models.CharField(max_length=36)),
                ('productid3', models.CharField(max_length=36)),
                ('logname3', models.CharField(max_length=328)),
                ('price3', models.CharField(max_length=36)),
                ('marketprice3', models.CharField(max_length=36)),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=64)),
                ('trackid', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'axf_shop',
            },
        ),
    ]
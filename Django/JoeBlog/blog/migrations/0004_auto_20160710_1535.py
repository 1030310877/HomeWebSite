# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-10 07:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20, null=True)),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('tags', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='column_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogColumn'),
        ),
    ]
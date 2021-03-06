# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 22:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields
import model_utils.fields
import quotes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('text', models.TextField()),
                ('author', models.ForeignKey(default=quotes.models.Author.get_default, on_delete=django.db.models.deletion.SET_DEFAULT, to='quotes.Author')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

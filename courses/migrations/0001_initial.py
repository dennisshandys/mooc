# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage
import courses.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
                ('level', models.CharField(max_length=50)),
                ('speaking_language', models.CharField(max_length=50)),
                ('transcript_language', models.CharField(max_length=50)),
                ('media', models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='E:\\Project\\uschools\\static\\protected'), upload_to=courses.models.download_media_location, null=True)),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]

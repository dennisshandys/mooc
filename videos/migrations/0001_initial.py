# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20161003_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=120)),
                ('embed_code', models.CharField(blank=True, null=True, max_length=500)),
                ('slug', models.SlugField(max_length=120)),
                ('description', models.TextField()),
                ('video_duration', models.DurationField(blank=True, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True, auto_now=True)),
                ('syllabus', models.ForeignKey(to='courses.Syllabus')),
            ],
        ),
    ]

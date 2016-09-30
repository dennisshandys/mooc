# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('email', models.EmailField(null=True, blank=True, max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prerequisite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=120)),
                ('short_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaggedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tag', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=120)),
                ('embed_code', models.CharField(null=True, blank=True, max_length=500)),
                ('slug', models.SlugField(max_length=120)),
                ('description', models.TextField()),
                ('featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('syllabus', models.ForeignKey(to='courses.Syllabus')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='taggeditem',
            name='course',
            field=models.ForeignKey(to='courses.Course'),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='course',
            field=models.ForeignKey(to='courses.Course'),
        ),
        migrations.AddField(
            model_name='prerequisite',
            name='course',
            field=models.ManyToManyField(to='courses.Course'),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='course',
            field=models.ManyToManyField(to='courses.Course'),
        ),
        migrations.AddField(
            model_name='course',
            name='organization',
            field=models.ForeignKey(to='courses.Organization', null=True),
        ),
    ]

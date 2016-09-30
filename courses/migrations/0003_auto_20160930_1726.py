# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import courses.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20160930_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('date', models.DateField()),
                ('line_no', models.IntegerField(max_length=120)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('enrollment_start', models.DateTimeField(null=True, auto_now_add=True)),
                ('enrollment_end', models.DateTimeField(null=True, auto_now_add=True)),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('testimony', models.TextField()),
                ('date', models.DateTimeField()),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('type', models.CharField(default='hd', choices=[('hd', 'HD'), ('sd', 'SD'), ('micro', 'Micro')], max_length=20)),
                ('height', models.CharField(blank=True, null=True, max_length=20)),
                ('width', models.CharField(blank=True, null=True, max_length=20)),
                ('media', models.ImageField(height_field='height', blank=True, width_field='width', null=True, upload_to=courses.models.thumbnail_location)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='video_duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='certificate',
            field=models.OneToOneField(to='courses.Certificate', blank=True, null=True),
        ),
    ]

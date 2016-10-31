# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_auto_20161024_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='effort',
            field=models.CharField(max_length=120, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='embed_code',
            field=models.CharField(max_length=500, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, to='courses.Institution'),
        ),
        migrations.AlterField(
            model_name='course',
            name='length_course',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='speaking_language',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=120, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='transcript_language',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='video_transcript',
            field=models.CharField(max_length=120, blank=True, null=True),
        ),
    ]

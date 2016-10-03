# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20161003_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectiveCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('what_you_learn', models.CharField(max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Organization',
            new_name='Institution',
        ),
        migrations.RemoveField(
            model_name='taggeditem',
            name='course',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='organization',
            new_name='institution',
        ),
        migrations.AddField(
            model_name='course',
            name='course_id',
            field=models.CharField(null=True, max_length=50),
        ),
        migrations.AddField(
            model_name='course',
            name='effort',
            field=models.CharField(null=True, max_length=120),
        ),
        migrations.AddField(
            model_name='course',
            name='length_course',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.CharField(null=True, max_length=50),
        ),
        migrations.AddField(
            model_name='course',
            name='video_transcript',
            field=models.CharField(null=True, max_length=120),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='occupation',
            field=models.CharField(null=True, max_length=120),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='title_degree',
            field=models.CharField(null=True, max_length=10),
        ),
        migrations.DeleteModel(
            name='TaggedItem',
        ),
        migrations.AddField(
            model_name='objectivecourse',
            name='course',
            field=models.ForeignKey(to='courses.Course'),
        ),
    ]

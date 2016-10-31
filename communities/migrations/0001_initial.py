# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import communities.models
from django.conf import settings
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0008_course_embed_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image_profile', models.ImageField(upload_to=communities.models.download_media_location, blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='E:\\Project\\uschools\\static\\protected'))),
                ('dob', models.DateField()),
                ('preferred_language', models.CharField(max_length=120, blank=True, null=True)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('interest', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=100, blank=True, null=True)),
                ('organization', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('website', models.URLField(blank=True, null=True)),
                ('about_me', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(null=True, auto_now=True)),
                ('facebook_link', models.CharField(max_length=320, blank=True, verbose_name='Facebook profile url', null=True)),
                ('twitter_handle', models.CharField(max_length=320, blank=True, verbose_name='Twitter handle', null=True)),
                ('related_course', models.ForeignKey(null=True, blank=True, to='courses.Course')),
                ('user_member', models.ForeignKey(related_name='member_hub', null=True, to=settings.AUTH_USER_MODEL)),
                ('user_owner', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage
import courses.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_auto_20161024_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='media',
            field=models.ImageField(upload_to=courses.models.download_media_location, storage=django.core.files.storage.FileSystemStorage(location='E:\\Project\\uschools\\static\\protected'), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='media',
            field=models.ImageField(upload_to=courses.models.download_media_profile_location, storage=django.core.files.storage.FileSystemStorage(location='E:\\Project\\uschools\\static\\protected'), null=True, blank=True),
        ),
    ]

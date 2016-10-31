# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage
import courses.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_auto_20161026_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='org',
            field=models.CharField(null=True, blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='media',
            field=models.ImageField(null=True, blank=True, storage=django.core.files.storage.FileSystemStorage(location='E:\\Project\\uschools\\static\\protected'), upload_to=courses.models.download_media_location),
        ),
    ]

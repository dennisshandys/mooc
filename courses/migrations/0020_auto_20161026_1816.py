# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import courses.models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_auto_20161026_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='media',
            field=models.ImageField(null=True, upload_to=courses.models.download_media_profile_location, blank=True, storage=django.core.files.storage.FileSystemStorage(location='E:\\Project\\uschools\\static\\protected')),
        ),
    ]

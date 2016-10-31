# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import accounts.models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20161010_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image_profile',
            field=models.ImageField(upload_to=accounts.models.download_media_location, storage=django.core.files.storage.FileSystemStorage(location='E:\\Project\\uschools\\static\\protected'), null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
    ]

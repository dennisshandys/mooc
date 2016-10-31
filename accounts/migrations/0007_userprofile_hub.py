# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0005_auto_20161018_1039'),
        ('accounts', '0006_auto_20161012_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='hub',
            field=models.ManyToManyField(to='communities.Hub'),
        ),
    ]

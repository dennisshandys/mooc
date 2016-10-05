# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20161005_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='title',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
    ]

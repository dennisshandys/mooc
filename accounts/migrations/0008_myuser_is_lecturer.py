# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_userprofile_hub'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_lecturer',
            field=models.BooleanField(default=False),
        ),
    ]

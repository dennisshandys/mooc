# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0005_auto_20161018_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hub',
            name='user_member',
        ),
    ]

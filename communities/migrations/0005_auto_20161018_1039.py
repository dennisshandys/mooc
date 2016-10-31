# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0004_auto_20161018_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hub',
            old_name='is_feautured',
            new_name='is_featured',
        ),
    ]

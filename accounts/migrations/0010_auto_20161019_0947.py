# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_lecturer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='Lecturer',
        ),
    ]

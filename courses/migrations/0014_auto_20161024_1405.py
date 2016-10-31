# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20161024_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='starting_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]

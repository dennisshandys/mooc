# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20161024_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='start_display',
            field=models.DateField(blank=True, null=True),
        ),
    ]

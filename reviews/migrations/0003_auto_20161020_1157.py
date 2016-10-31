# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_testimony_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimony',
            name='date',
        ),
        migrations.AlterField(
            model_name='testimony',
            name='course',
            field=models.ForeignKey(null=True, blank=True, to='courses.Course'),
        ),
    ]

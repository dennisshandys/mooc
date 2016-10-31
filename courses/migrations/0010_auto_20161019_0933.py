# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20161019_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='course',
        ),
        migrations.AlterField(
            model_name='course',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Lecturer',
        ),
    ]

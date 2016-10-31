# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='embed_code',
            field=models.CharField(max_length=500, null=True),
        ),
    ]

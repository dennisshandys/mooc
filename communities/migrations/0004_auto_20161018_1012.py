# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0003_auto_20161018_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub',
            name='user_member',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='member_hub'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communities', '0002_hub_is_feautured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hub',
            name='user_member',
        ),
        migrations.AddField(
            model_name='hub',
            name='user_member',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='member_hub', null=True),
        ),
    ]

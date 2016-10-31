# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coachingcircle',
            name='user',
            field=models.ManyToManyField(to='accounts.UserProfile'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20160930_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='line_no',
            field=models.IntegerField(),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20161003_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('review_text', models.TextField()),
                ('date', models.DateTimeField()),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True, auto_now=True)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
        ),
    ]

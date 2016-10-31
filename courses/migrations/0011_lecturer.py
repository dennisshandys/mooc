# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20161019_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('occupation', models.CharField(null=True, max_length=120)),
                ('title_degree', models.CharField(null=True, max_length=10)),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('course', models.ManyToManyField(to='courses.Course')),
            ],
        ),
    ]

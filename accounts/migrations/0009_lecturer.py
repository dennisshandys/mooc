# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_myuser_is_lecturer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('occupation', models.CharField(max_length=120, null=True)),
                ('title_degree', models.CharField(max_length=10, null=True)),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True, auto_now=True)),
                ('user_profile', models.OneToOneField(to='accounts.UserProfile')),
            ],
        ),
    ]

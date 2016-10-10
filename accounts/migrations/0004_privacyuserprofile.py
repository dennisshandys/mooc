# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20161005_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyUserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('is_dob', models.BooleanField(default=False)),
                ('preferred_language', models.BooleanField(default=False)),
                ('address', models.BooleanField(default=False)),
                ('city', models.BooleanField(default=False)),
                ('country', models.BooleanField(default=False)),
                ('zip_code', models.BooleanField(default=False)),
                ('interest', models.BooleanField(default=False)),
                ('title', models.BooleanField(default=False)),
                ('organization', models.BooleanField(default=False)),
                ('email', models.BooleanField(default=False)),
                ('phone', models.BooleanField(default=False)),
                ('website', models.BooleanField(default=False)),
                ('about_me', models.BooleanField(default=False)),
                ('facebook_link', models.BooleanField(default=False)),
                ('twitter_handle', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]

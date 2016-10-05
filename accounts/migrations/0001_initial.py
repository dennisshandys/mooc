# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('username', models.CharField(unique=True, max_length=255)),
                ('email', models.EmailField(verbose_name='email address', unique=True, max_length=255)),
                ('first_name', models.CharField(blank=True, null=True, max_length=120)),
                ('last_name', models.CharField(blank=True, null=True, max_length=120)),
                ('is_member', models.BooleanField(verbose_name='Is Paid Member', default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(blank=True, null=True, max_length=120)),
                ('last_name', models.CharField(blank=True, null=True, max_length=120)),
                ('dob', models.DateField()),
                ('preferred_language', models.CharField(blank=True, null=True, max_length=120)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('interest', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('organization', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('website', models.URLField(blank=True, null=True)),
                ('about_me', models.TextField(blank=True, null=True)),
                ('facebook_link', models.CharField(verbose_name='Facebook profile url', blank=True, null=True, max_length=320)),
                ('twitter_handle', models.CharField(verbose_name='Twitter handle', blank=True, null=True, max_length=320)),
                ('user', models.OneToOneField(to='accounts.MyUser')),
            ],
        ),
    ]

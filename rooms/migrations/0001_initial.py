# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_auto_20161024_1511'),
        ('accounts', '0011_remove_myuser_is_lecturer'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoachingCircle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, null=True, max_length=50)),
                ('room_number', models.IntegerField()),
                ('time_available', models.CharField(blank=True, null=True, choices=[('08:00-09:30 AM', '08:00-09:30 AM'), ('09:30-11:00 AM', '09:30-11:00 AM'), ('11:00-12:30 PM', '11:00-12:30 PM'), ('12:30-02:00 PM', '12:30-02:00 PM'), ('02:00-03:30 PM', '02:00-03:30 PM'), ('03:30-05:00 PM', '03:30-05:00 PM'), ('05:00-06:30 PM', '05:00-06:30 PM'), ('06:30-08:00 PM', '06:30-08:00 PM'), ('08:00-09:30 PM', '08:00-09:30 PM'), ('09:30-11:00 PM', '09:30-11:00 PM')], max_length=50)),
                ('day_available', models.CharField(blank=True, null=True, choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=50)),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True, auto_now=True)),
                ('course', models.ForeignKey(to='courses.Course')),
                ('user', models.ManyToManyField(blank=True, null=True, to='accounts.UserProfile')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_privacyuserprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='privacyuserprofile',
            old_name='about_me',
            new_name='is_about_me',
        ),
        migrations.RenameField(
            model_name='privacyuserprofile',
            old_name='address',
            new_name='is_address',
        ),
        migrations.RenameField(
            model_name='privacyuserprofile',
            old_name='city',
            new_name='is_city',
        ),
        migrations.RenameField(
            model_name='privacyuserprofile',
            old_name='country',
            new_name='is_country',
        ),
        migrations.RenameField(
            model_name='privacyuserprofile',
            old_name='email',
            new_name='is_email',
        ),
        migrations.RenameField(
            model_name='privacyuserprofile',
            old_name='facebook_link',
            new_name='is_facebook_link',
        ),
        migrations.RenameField(
            model_name='privacyuserprofile',
            old_name='interest',
            new_name='is_interest',
        ),
        migrations.RenameField(
            model_name='privacyuserprofile',
            old_name='organization',
            new_name='is_notif_assesment',
        ),
        migrations.RenameField(
            model_name='privacyuserprofile',
            old_name='phone',
            new_name='is_notif_pm',
        ),
        migrations.RenameField(
            model_name='privacyuserprofile',
            old_name='preferred_language',
            new_name='is_organization',
        ),
        migrations.RenameField(
            model_name='privacyuserprofile',
            old_name='title',
            new_name='is_phone',
        ),
        migrations.RenameField(
            model_name='privacyuserprofile',
            old_name='twitter_handle',
            new_name='is_preferred_language',
        ),
        migrations.RenameField(
            model_name='privacyuserprofile',
            old_name='website',
            new_name='is_private_message',
        ),
        migrations.RenameField(
            model_name='privacyuserprofile',
            old_name='zip_code',
            new_name='is_title',
        ),
        migrations.AddField(
            model_name='privacyuserprofile',
            name='is_twitter_handle',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='privacyuserprofile',
            name='is_user_profile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='privacyuserprofile',
            name='is_website',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='privacyuserprofile',
            name='is_zip_code',
            field=models.BooleanField(default=False),
        ),
    ]

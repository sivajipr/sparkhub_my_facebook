# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20150608_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='userimage',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userimage',
            name='is_active_cover',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='is_active_profile',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]

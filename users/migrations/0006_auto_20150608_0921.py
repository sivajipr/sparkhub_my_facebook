# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150608_0916'),
    ]

    operations = [
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
    ]

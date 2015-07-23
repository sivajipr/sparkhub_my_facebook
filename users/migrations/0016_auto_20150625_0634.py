# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20150625_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=b'profiles/', blank=True),
        ),
    ]

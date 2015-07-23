# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20150625_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='profile_pic',
            field=models.ImageField(default=b'profiles/default_image.jpg', null=True, upload_to=b'profiles/', blank=True),
        ),
    ]

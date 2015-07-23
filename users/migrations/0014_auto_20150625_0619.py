# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20150623_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='profile_pic',
            field=models.ImageField(default=b'static/image/default_image.jpg', null=True, upload_to=b'profiles/', blank=True),
        ),
    ]

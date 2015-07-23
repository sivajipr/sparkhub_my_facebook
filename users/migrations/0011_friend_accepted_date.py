# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20150618_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='accepted_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

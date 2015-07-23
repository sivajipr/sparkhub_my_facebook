# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20150529_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_pic', models.ImageField(null=True, upload_to=b'profiles/', blank=True)),
                ('cover_pic', models.ImageField(null=True, upload_to=b'covers/', blank=True)),
                ('is_active_profile', models.BooleanField(default=False)),
                ('is_active_cover', models.BooleanField(default=False)),
                ('is_public', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]

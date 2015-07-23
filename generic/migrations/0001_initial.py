# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_gallery'),
        ('event', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=600)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(related_name=b'event_comments', blank=True, to='event.Event', null=True)),
                ('post', models.ForeignKey(related_name=b'post_comments', blank=True, to='Post.Post', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(related_name=b'event_likes', blank=True, to='event.Event', null=True)),
                ('post', models.ForeignKey(related_name=b'post_likes', blank=True, to='Post.Post', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

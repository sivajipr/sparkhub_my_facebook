from django.db import models
from django.contrib.auth.models import User
from Post.models import Post
from event.models import Event
# Create your models here.

class Like(models.Model):
	user = models.ForeignKey(User)
	post = models.ForeignKey('Post.Post', related_name = "post_likes", null=True, blank=True)
	event = models.ForeignKey('event.Event', related_name = "event_likes", null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
	comment = models.CharField(max_length=600)
	user = models.ForeignKey(User)
	post = models.ForeignKey('Post.Post', related_name = "post_comments", null=True, blank=True)
	event = models.ForeignKey('event.Event', related_name = "event_comments", null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
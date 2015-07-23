from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField(max_length=300)
	user = models.ForeignKey(User)
	create_date = models.DateTimeField(auto_now_add=True)

	@property
	def get_attach(self):
	    return [i for i in self.post_attach.all().order_by('-create_date')[:3]]

	@property
	def get_likecount(self):
	    return self.post_likes.count()

	@property
	def get_comments(self):
	    return [i for i in self.post_comments.all().order_by('-create_date')[:3]][::-1]

class Gallery(models.Model):
	post = models.ForeignKey('Post', related_name = "post_attach", null=True, blank=True)
	url = models.CharField(max_length=1000, null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)

	def __unicode__ (self):
		return self.post.title if self.post and self.post.title else None
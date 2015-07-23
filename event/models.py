from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
	title = models.CharField(max_length=50)
	start_date = models.DateField()
	end_date = models.DateField()
	create_date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User)

	@property
	def get_attendies(self):
		return [i.user for i in self.event_name.all()]

	@property
	def get_attach(self):
	    return [i for i in self.event_attach.all().order_by('-create_date')[:3]]

	@property
	def get_eventlikecount(self):
	    return self.event_likes.count()

	@property
	def get_comments(self):
	    return [i for i in self.event_comments.all().order_by('-create_date')[:3]][::-1]
	

class Relation(models.Model):
	user = models.ForeignKey(User)
	event = models.ForeignKey('Event', related_name = "event_name")
	create_date = models.DateTimeField(auto_now_add=True)

	def __unicode__ (self):
		return self.event.title

class Picture(models.Model):
	event = models.ForeignKey('Event', related_name = "event_attach", null=True, blank=True)
	url = models.CharField(max_length=1000, null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User)
	place = models.CharField(max_length=200)
	
	@property
	def get_avatar(self):
		if self.user.userimage_set.filter(is_active_profile=True, is_public=True).exists():
			return self.user.userimage_set.filter(is_active_profile=True, is_public=True)[0].profile_pic
		return 'profiles/default_image.jpg'

	@property
	def get_cover(self):
		if self.user.userimage_set.filter(is_active_cover=True, is_public=True).exists():
			return self.user.userimage_set.filter(is_active_cover=True, is_public=True)[0].cover_pic
		return 'covers/default_cover.jpg'

	@property
	def get_post(self):
		return [i for i in self.user.post_set.all().order_by('-create_date')]
	
	@property
	def get_event(self):
		return [i for i in self.user.event_set.all().order_by('-create_date')]
	
	def get_friends(self):
		return [i.creator for i in self.user.friend_set.filter(status=1)]+ [i.acceptor for i in self.user.friendship_creator_set.filter(status=1)]            

class UserImage(models.Model):
	user = models.ForeignKey(User)
	profile_pic = models.ImageField(upload_to="profiles/", null=True, blank=True)
	cover_pic = models.ImageField(upload_to="covers/", null=True, blank=True)
	is_active_profile = models.BooleanField(default=False)
	is_active_cover = models.BooleanField(default=False)
	is_public = models.BooleanField(default=False)
	create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Friend(models.Model):
	creator = models.ForeignKey(User, related_name="friendship_creator_set")
	acceptor = models.ForeignKey(User, related_name="friend_set")
	status = models.IntegerField(default=0)
	create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	accepted_date = models.DateTimeField(null=True, blank=True)

	

def create_profile(sender, instance, created, raw, **kwargs):
	"""Fleshes out the profile for the newly created user"""
	if created:
		profile = Profile(user=instance)
		profile.save()

post_save.connect(create_profile, sender=User,
dispatch_uid='users.models.create_profile')
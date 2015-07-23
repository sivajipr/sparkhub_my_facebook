from django.contrib import admin
from users.models import *
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'place')

class UserImageAdmin(admin.ModelAdmin):
	list_display = ('user', 'profile_pic', 'cover_pic')

class FriendAdmin(admin.ModelAdmin):
	list_display = ('creator','acceptor', 'status')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserImage, UserImageAdmin)
admin.site.register(Friend, FriendAdmin)
from django.contrib import admin
from generic.models import Like, Comment
# Register your models here.

class LikeAdmin(admin.ModelAdmin):
	list_display=('user','post','event','create_date')

class CommentAdmin(admin.ModelAdmin):
	list_display=('user','comment', 'post','event','create_date')

admin.site.register(Like,LikeAdmin)
admin.site.register(Comment,CommentAdmin)
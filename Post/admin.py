from django.contrib import admin
from Post.models import Post,Gallery
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('user','title', 'text', 'create_date')

class GalleryAdmin(admin.ModelAdmin):
	list_display = ('post','url', 'create_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Gallery, GalleryAdmin)



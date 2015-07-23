from django.contrib import admin
from event.models import Event, Picture

# Register your models here.
class EventAdmin(admin.ModelAdmin):
	list_display=('user','title','start_date', 'create_date')

class PictureAdmin(admin.ModelAdmin):
	list_display=('event', 'url', 'create_date')

admin.site.register(Event,EventAdmin)
admin.site.register(Picture,PictureAdmin)
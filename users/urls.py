from django.conf.urls import patterns, include, url
import views
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spark_hub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.register),
    url(r'^home', views.home),
    url(r'^logout', views.log_out),
    url(r'^users/editprofile', views.edit_profile),
    url(r'^usersearch', views.usersearch),
    url(r'^autocomplete', views.auto_complete),
    url(r'^user/(?P<id>[0-9]{1,})/request',views.addfriend, name="addfriend"),
    url(r'^user/(?P<id>[0-9]{1,})/accept',views.accept, name="accept"),
    url(r'^user/(?P<id>[0-9]{1,})/reject',views.reject, name="reject"),
    
)

if settings.DEBUG:
   urlpatterns = patterns('',
   url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
   url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
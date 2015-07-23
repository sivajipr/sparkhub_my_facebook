from django.conf.urls import patterns, include, url
from django.contrib import admin
from users.views import user_page, user_pic_show, user_friend_list, user_friend_request
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spark_hub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('users.urls')),
    url(r'^', include('Post.urls')),
    url(r'^', include('generic.urls')),
    url(r'^', include('event.urls')),
    url(r'^login', 'django.contrib.auth.views.login'),
    url(r'^(?P<user>\w+)/photos',user_pic_show),
    url(r'^(?P<user>\w+)/friends',user_friend_list),
    url(r'^(?P<user>\w+)/friend_request',user_friend_request),
    url(r'^(?P<user>\w+)',user_page, name="user-page"),
)

from django.conf.urls import patterns, include, url
import views
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spark_hub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^post/(?P<id>[0-9]{1,})/like',views.like_post, name="post-like"),
	url(r'^post/(?P<id>[0-9]{1,})/unlike',views.unlike_post, name="post-unlike"),
    url(r'^post/(?P<id>[0-9]{1,})/comment',views.comment_post, name="post-comment"),
    url(r'^event/(?P<id>[0-9]{1,})/like',views.like_event, name="event-like"),
	url(r'^event/(?P<id>[0-9]{1,})/unlike',views.unlike_event, name="event-unlike"),
	url(r'^event/(?P<id>[0-9]{1,})/comment',views.comment_event, name="event-comment"),
)
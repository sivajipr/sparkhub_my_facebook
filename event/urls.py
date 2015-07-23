from django.conf.urls import patterns, include, url
import views
import users
from Post.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spark_hub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^event/createevent', views.create_event),
    url(r'^event/allevent', views.all_event),
    url(r'^event/myevent', views.my_event),
    url(r'^event/attend/(?P<id>[0-9]{1,})',views.attend),
    url(r'^event/attendingevent',views.attending_event),
)

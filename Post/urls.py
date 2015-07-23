from django.conf.urls import patterns, include, url
import views
import users
from Post.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spark_hub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^post/createpost', views.create_post, name="create_post" ),
    url(r'^post/myposts', users.views.showpost),
    url(r'upload/',upload,name='upload'),
)

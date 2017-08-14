from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from steemfriend import settings
from . import views

app_name = 'friend'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^find_friends/$', views.find_friends, name='find_friends'),
    # url(r'^(?P<account>[a-zA-Z]+)/friends/$', views.friends_results, name='friends_results'),
]

urlpatterns += staticfiles_urlpatterns()

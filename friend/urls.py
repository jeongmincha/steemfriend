from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from steemfriend import settings
from . import views

app_name = 'friend'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<account>[a-zA-Z]+)/friends/$', views.friends, name='friends'),
]

urlpatterns += staticfiles_urlpatterns()

from django.conf.urls import patterns, url

from .views import upload
from .views import thanks


urlpatterns = patterns('',
    url(r'^upload/(\w+)/$', upload, name='upload'),
    url(r'^thanks/$', thanks, name='thanks'),
)

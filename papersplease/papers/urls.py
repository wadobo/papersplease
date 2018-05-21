from django.conf.urls import url

from .views import upload
from .views import thanks


urlpatterns = [
    url(r'^upload/(\w+)/$', upload, name='upload'),
    url(r'^thanks/$', thanks, name='thanks'),
]

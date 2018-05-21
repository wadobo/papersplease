from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', static.serve, { 'document_root': settings.MEDIA_ROOT }),
    url(r'', include('papers.urls')),
]

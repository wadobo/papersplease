from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import Paper


class Upload(TemplateView):
    template_name = 'upload.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(Upload, self).get_context_data(*args, **kwargs)
        ctx['paper'] = self.paper
        return ctx

    def get(self, request, key):
        self.paper = get_object_or_404(Paper, url=key)
        return super(Upload, self).get(request)

    def post(self, request, key):
        self.paper = get_object_or_404(Paper, url=key)
        return super(Upload, self).post(request)

upload = Upload.as_view()

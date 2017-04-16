from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import Http404

from .models import Paper
from .models import Attachment


class Upload(TemplateView):
    template_name = 'upload.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(Upload, self).get_context_data(*args, **kwargs)
        ctx['paper'] = self.paper
        return ctx

    def get(self, request, key):
        if not key.strip():
            raise Http404("Not found")

        self.paper = get_object_or_404(Paper, url=key)
        return super(Upload, self).get(request)

    def post(self, request, key):
        paper = get_object_or_404(Paper, url=key)

        if not 'attach' in request.FILES:
            return redirect('upload', key)

        attach = Attachment(paper=paper,
                            attach=request.FILES['attach'])
        attach.save()

        paper.status = 'uploaded'
        paper.url = ''
        paper.save()

        return redirect('thanks')

upload = Upload.as_view()


class Thanks(TemplateView):
    template_name = 'thanks.html'
thanks = Thanks.as_view()

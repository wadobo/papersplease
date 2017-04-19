from __future__ import unicode_literals

import os
import io
import tarfile
from functools import partial

from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages

from .models import PAPER_CHOICES


paper_actions = []

def send_email(modeladmin, request, queryset):
    for p in queryset:
        p.url = p.gen_url()
        p.save()


        email_body = settings.PAPERS_EMAIL_BODY
        url = '{0}/upload/{1}'.format(settings.PAPERS_URL, p.url)
        subject = settings.PAPERS_EMAIL_SUBJECT
        message = email_body.format(paper=p.title,
                                    conf=p.conference.name,
                                    url=url)

        p.email(subject, message)

    messages.success(request, '{0} Emails sent.'.format(queryset.count()))


def download(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/gzip")
    response['Content-Disposition'] = 'attachment; filename="papers.tar.gz"'

    files = []
    for p in queryset:
        files += [i.attach.path for i in p.attachs.all()]

    output = io.BytesIO()
    tar = tarfile.open(fileobj=output, mode='w:gz')

    def reset(tarinfo):
        name = os.path.basename(tarinfo.name)
        _, d = os.path.split(os.path.dirname(tarinfo.name))
        tarinfo.name = os.path.join(d, name)
        return tarinfo

    for f in files:
        tar.add(f, filter=reset)
    tar.close()

    output.seek(0)
    response.content = output.read()

    return response


paper_actions.append(download)
paper_actions.append(send_email)


def set_status(modeladmin, request, queryset, key='missing'):
    queryset.update(status=key)

for k, v in PAPER_CHOICES:
    action = partial(set_status, key=k)
    action.short_description = u"Set status to '{0}'".format(v)
    action.__name__ = 'set_{0}'.format(k)
    paper_actions.append(action)

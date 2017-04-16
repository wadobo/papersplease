from __future__ import unicode_literals

import os
import io
import tarfile

from django.http import HttpResponse
from .models import PAPER_CHOICES
from functools import partial


paper_actions = []


email_body = '''
Hello,

You're receiving this email because you are the author of the paper:
{paper}

for the conference:
{conf}

Please, send us the corresponding file using the following url:
{url}

Note: This path is a one-use-then-drop, so once you upload your paper, this
url will be invalid.

Regards.
'''


def send_email(modeladmin, request, queryset):
    for p in queryset:
        p.url = p.gen_url()
        p.save()


        # TODO: make this configurable
        url = 'http://localhost:8000/upload/{0}'.format(p.url)
        subject = 'Your papers, please'
        message = email_body.format(paper=p.title,
                                    conf=p.conference.name,
                                    url=url)

        p.email(subject, message)


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

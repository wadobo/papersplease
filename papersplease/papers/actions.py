from __future__ import unicode_literals

from .models import PAPER_CHOICES
from functools import partial


paper_actions = []

def set_status(modeladmin, request, queryset, key='missing'):
    queryset.update(status=key)

for k, v in PAPER_CHOICES:
    action = partial(set_status, key=k)
    action.short_description = u"Set status to '{0}'".format(v)
    action.__name__ = 'set_{0}'.format(k)
    paper_actions.append(action)


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

paper_actions.append(send_email)

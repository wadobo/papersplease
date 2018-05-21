from __future__ import print_function
from __future__ import unicode_literals

from os import path
from django.db import models
from django.core.mail import send_mail
import random


PAPER_CHOICES = (
    ('missing', 'Paper Missing'),
    ('uploaded', 'Paper Uploaded'),
    ('claimed', 'Being Reviewed'),
    ('changes', 'Changes Requested'),
    ('ready', 'Camera Ready'),
)

#  state machine:
#            action taken                new state
#######################################################################################
#  Initial   create paper:               'missing'  -> and email sent inviting upload
#            upload paper:               'uploaded'
#            reviewer downloads:         'claimed'
#            reviewer asks for changes:  'changes' -> and email sent inviting upload
#  Final     reviewer accepts:           'ready'

def paper_path(instance, filename):
    conf = instance.paper.conference.slug
    fname = instance.paper.slug
    _, ext = path.splitext(filename)
    return 'papers/{0}/{1}{2}'.format(conf, fname, ext)


class Author(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u'{0} <{1}>'.format(self.get_full_name(), self.email)


class Conference(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    place = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['date']


class Paper(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    status = models.CharField(max_length=10, choices=PAPER_CHOICES, default='missing')
    conference = models.ForeignKey(Conference, related_name="papers", on_delete=models.PROTECT)
    authors = models.ManyToManyField(Author, related_name="papers")

    url = models.CharField(max_length=80, blank=True)

    def gen_url(self):
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return ''.join(random.choice(chars) for i in range(80))

    def email(self, subject, message, from_email=None, **kwargs):
        to = [i.email for i in self.authors.all()]
        send_mail(subject, message, from_email, to, **kwargs)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.title


class Attachment(models.Model):
    paper = models.ForeignKey(Paper, related_name="attachs", on_delete=models.PROTECT)
    attach = models.FileField(upload_to=paper_path)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.attach.path

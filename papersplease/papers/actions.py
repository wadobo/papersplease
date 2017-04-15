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

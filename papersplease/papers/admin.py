from __future__ import print_function
from __future__ import unicode_literals

from django.contrib import admin

from .models import Conference
from .models import Paper
from .models import Author
from .models import Attachment

from .actions import paper_actions


class AttachInline(admin.TabularInline):
    model = Attachment


class ConferenceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'place', 'date')

    search_fields = ('name', 'place')
    date_hierarchy = 'date'


class PaperAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'conference', 'status', 'pauthors',
                    'hasattach')

    list_filter = ('status', 'conference')
    search_fields = ('title', 'conference__name', 'conference__place',
                     'authors__first_name',
                     'authors__last_name', 'authors__email')

    filter_horizontal = ('authors', )
    inlines = [AttachInline, ]

    actions = paper_actions

    def pauthors(self, obj):
        return ', '.join(i.get_full_name() for i in obj.authors.all())
    pauthors.short_description = 'Authors'

    def hasattach(self, obj):
        return obj.attachs.exists()
    hasattach.short_description = 'Attach?'
    hasattach.boolean = True


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')

class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('attach', 'paper', 'uploaded')


admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Paper, PaperAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Attachment, AttachmentAdmin)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import papers.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attach', models.FileField(upload_to=papers.models.paper_path)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, blank=True)),
                ('last_name', models.CharField(max_length=50, blank=True)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200, blank=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=200)),
                ('status', models.CharField(default=b'missing', max_length=10, choices=[(b'missing', b'Paper Missing'), (b'changes', b'Changes Requested'), (b'uploaded', b'Paper Uploaded'), (b'ready', b'Camera Ready')])),
                ('authors', models.ManyToManyField(related_name='papers', to='papers.Author')),
                ('conference', models.ForeignKey(related_name='papers', to='papers.Conference', on_delete=models.PROTECT)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='attachment',
            name='paper',
            field=models.ForeignKey(related_name='attachs', to='papers.Paper', on_delete=models.PROTECT),
            preserve_default=True,
        ),
    ]

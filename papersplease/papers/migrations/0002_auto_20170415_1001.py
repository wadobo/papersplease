# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conference',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='paper',
            name='url',
            field=models.CharField(max_length=80, blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_auto_20170415_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='status',
            field=models.CharField(default='missing', max_length=10, choices=[('missing', 'Paper Missing'), ('uploaded', 'Paper Uploaded'), ('claimed', 'Being Reviewed'), ('changes', 'Changes Requested'), ('ready', 'Camera Ready')]),
            preserve_default=True,
        ),
    ]

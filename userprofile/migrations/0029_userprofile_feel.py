# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0028_delete_feeds'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='feel',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
    ]

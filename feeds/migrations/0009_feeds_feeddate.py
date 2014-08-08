# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0008_delete_feel'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeds',
            name='feeddate',
            field=models.DateTimeField(default=datetime.datetime(2014, 7, 29, 2, 51, 6, 435095)),
            preserve_default=True,
        ),
    ]

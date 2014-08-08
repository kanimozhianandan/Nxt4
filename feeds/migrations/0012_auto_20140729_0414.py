# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0011_auto_20140729_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

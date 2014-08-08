# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0010_auto_20140729_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='video',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='feeds',
            name='adddate',
            field=models.DateField(default=datetime.date.today, blank=True),
        ),
        migrations.AlterField(
            model_name='feeds',
            name='postdate',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]

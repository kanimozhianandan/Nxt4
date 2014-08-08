# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0026_auto_20140727_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='postdate',
            field=models.DateField(verbose_name=datetime.datetime(2014, 7, 27, 3, 25, 35, 496816)),
        ),
    ]

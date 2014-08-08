# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='postdate',
            field=models.DateField(verbose_name=datetime.datetime(2014, 7, 27, 4, 8, 21, 296780)),
        ),
    ]

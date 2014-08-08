# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_auto_20140727_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='postdate',
            field=models.DateField(verbose_name=datetime.datetime(2014, 7, 28, 2, 40, 58, 813504)),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_auto_20140704_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='athlete',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0019_auto_20140707_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='graduation_year',
        ),
    ]

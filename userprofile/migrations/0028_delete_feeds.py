# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0027_auto_20140727_0325'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feeds',
        ),
    ]

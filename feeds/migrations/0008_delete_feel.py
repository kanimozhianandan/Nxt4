# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0007_auto_20140729_0232'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feel',
        ),
    ]

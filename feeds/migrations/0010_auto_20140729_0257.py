# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0009_feeds_feeddate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feeds',
            name='feeddate',
        ),
        migrations.AlterField(
            model_name='feeds',
            name='postdate',
            field=models.DateField(null=True),
        ),
    ]

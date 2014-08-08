# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0006_feel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='postdate',
            field=models.DateField(auto_now_add=True),
        ),
    ]

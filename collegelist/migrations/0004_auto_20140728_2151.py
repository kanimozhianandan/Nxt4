# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collegelist', '0003_auto_20140714_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegelist',
            name='college_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

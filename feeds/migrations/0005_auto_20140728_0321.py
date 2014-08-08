# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20140728_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id'),
        ),
    ]

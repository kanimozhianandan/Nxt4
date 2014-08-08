# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('collegelist', '0004_auto_20140728_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegelist',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id'),
        ),
    ]

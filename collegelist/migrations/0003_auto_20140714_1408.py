# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('collegelist', '0002_auto_20140708_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegelist',
            name='college_name',
            field=models.CharField(default=b'Boston University', max_length=100),
        ),
        migrations.AlterField(
            model_name='collegelist',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', unique=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_auto_20140728_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='adddate',
            field=models.DateField(default=datetime.date.today, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='feeds',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', unique=True),
        ),
        migrations.AlterField(
            model_name='feeds',
            name='postdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='feeds',
            name='postto',
            field=models.CharField(max_length=15, null=True, choices=[(b'Students', b'Students'), (b'Counselors', b'Counselors'), (b'Everyone', b'Everyone')]),
        ),
    ]

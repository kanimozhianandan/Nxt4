# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
import feeds.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('feed', models.CharField(max_length=1050)),
                ('postdate', models.DateField(verbose_name=datetime.datetime(2014, 7, 27, 4, 0, 56, 407270))),
                ('video', models.FileField(null=True, upload_to=feeds.models.genvideo_file, blank=True)),
                ('adddate', models.DateField(default=datetime.date.today, blank=True)),
                ('postto', models.CharField(max_length=15, choices=[(b'Students', b'Students'), (b'Counselors', b'Counselors'), (b'Everyone', b'Everyone')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

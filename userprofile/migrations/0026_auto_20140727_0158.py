# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userprofile.models
import feeds.models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0025_userprofile_pp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('feed', models.CharField(max_length=1050)),
                ('postdate', models.DateField(verbose_name=datetime.datetime(2014, 7, 27, 1, 58, 5, 125279))),
                ('video', models.FileField(null=True, upload_to=feeds.models.genvideo_file, blank=True)),
                ('adddate', models.DateField(default=datetime.date.today, blank=True)),
                ('postto', models.CharField(max_length=15, choices=[(b'Students', b'Students'), (b'Counselors', b'Counselors'), (b'Everyone', b'Everyone')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='volunteer',
            field=models.CharField(max_length=350, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sports',
            field=models.CharField(max_length=75, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='year_in_school',
            field=models.CharField(max_length=10, choices=[(b'Freshman', b'Freshman'), (b'Sophomore', b'Sophomore'), (b'Junior', b'Junior'), (b'Senior', b'Senior')]),
        ),
    ]

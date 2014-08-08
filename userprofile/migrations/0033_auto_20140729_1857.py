# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0032_auto_20140729_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pp',
            field=models.ImageField(default=b'/static/img/nxtwhite.jpg', null=True, upload_to=userprofile.models.gen_file),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='year_in_school',
            field=models.CharField(default=b'Freshman', max_length=15, null=True, choices=[(b'Freshman', b'Freshman'), (b'Sophomore', b'Sophomore'), (b'Junior', b'Junior'), (b'Senior', b'Senior')]),
        ),
    ]

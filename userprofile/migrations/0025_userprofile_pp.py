# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0024_remove_userprofile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pp',
            field=models.ImageField(default=b'/static/img/nxtwhite.jpg', upload_to=userprofile.models.gen_file),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0022_auto_20140707_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pic',
            field=models.ImageField(default=b'picturz/no-img.jpg', upload_to=b'picturz/'),
            preserve_default=True,
        ),
    ]

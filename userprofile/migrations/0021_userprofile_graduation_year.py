# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0020_remove_userprofile_graduation_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='graduation_year',
            field=models.IntegerField(max_length=4, null=True, choices=[(2015, 2015), (2016, 2016), (2017, 2017)]),
            preserve_default=True,
        ),
    ]

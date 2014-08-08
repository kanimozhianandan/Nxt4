# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0029_userprofile_feel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='year_in_school',
            field=models.CharField(max_length=15, null=True, choices=[(b'Freshman', b'Freshman'), (b'Sophomore', b'Sophomore'), (b'Junior', b'Junior'), (b'Senior', b'Senior')]),
        ),
    ]

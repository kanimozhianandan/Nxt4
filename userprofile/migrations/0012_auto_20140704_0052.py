# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0011_userprofile_clubs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='clubs',
            new_name='club',
        ),
    ]

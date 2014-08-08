# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0014_userprofile_graduation_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='club',
            new_name='clubs',
        ),
    ]

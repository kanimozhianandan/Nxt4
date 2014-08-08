# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0030_auto_20140728_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='feel',
            field=models.CharField(max_length=10, null=True, choices=[(b'Yippeee!', b'Yippeee!'), (b':)', b':)'), (b':(', b':('), (b"'SUP", b'SUP'), (b'Kewl!', b'Kewl!'), (b'BRB', b'BRB'), (b':D', b':D')]),
        ),
    ]

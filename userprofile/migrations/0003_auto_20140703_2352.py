# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20140702_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='clubs',
            field=models.CharField(help_text=b'Clubs in school', max_length=150, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='athlete',
            field=models.CharField(default=b'No', max_length=1, choices=[(1, b'athlete')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sports',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
    ]

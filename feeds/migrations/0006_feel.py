# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0005_auto_20140728_0321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('feel', models.CharField(max_length=10, null=True, choices=[(b'Yippeee!', b'Yippeee!'), (b':)', b':)'), (b':(', b':('), (b"'SUP", b'SUP'), (b'Kewl!', b'Kewl!'), (b'BRB', b'BRB'), (b':D', b':D')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

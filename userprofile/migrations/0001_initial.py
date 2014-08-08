# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', unique=True)),
                ('birth_date', models.DateField(blank=True)),
                ('counselor_email', models.EmailField(max_length=75)),
                ('year_in_school', models.CharField(max_length=15)),
                ('interests', models.CharField(max_length=75)),
                ('sports', models.CharField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

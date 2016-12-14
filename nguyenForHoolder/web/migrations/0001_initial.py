# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userName', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('fullName', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('age', models.CharField(max_length=250)),
                ('sport', models.CharField(max_length=250)),
                ('book', models.CharField(max_length=250)),
            ],
        ),
    ]

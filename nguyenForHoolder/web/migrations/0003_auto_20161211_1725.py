# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20161211_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='userSS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userName', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('fullName', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('age', models.CharField(max_length=250)),
                ('sport', models.CharField(max_length=250)),
                ('book', models.CharField(max_length=250)),
                ('cinema', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]

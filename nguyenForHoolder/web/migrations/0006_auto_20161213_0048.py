# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20161211_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='age',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='book',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='cinema',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='fullName',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='sport',
        ),
    ]

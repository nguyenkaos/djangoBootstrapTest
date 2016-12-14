# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20161211_1725'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='userSS',
            new_name='utilisateur',
        ),
    ]

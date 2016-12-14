# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20161211_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='age',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='book',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='cinema',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='email',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='sport',
            field=models.CharField(max_length=250, blank=True),
        ),
    ]

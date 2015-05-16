# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_auto_20150515_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='asociado',
            name='slug',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

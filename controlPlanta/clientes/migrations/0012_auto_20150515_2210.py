# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0011_auto_20150515_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='associated_code',
            field=models.PositiveIntegerField(unique=True, null=True, verbose_name=b'N\xc3\xbamero de asociado', blank=True),
        ),
    ]

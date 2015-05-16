# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0012_auto_20150515_2210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['id'], 'verbose_name_plural': '1. Clientes'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='identification',
            field=models.CharField(max_length=255, unique=True, null=True, verbose_name=b'C\xc3\xa9dula', blank=True),
        ),
    ]

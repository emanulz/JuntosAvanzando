# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20150515_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='bar_code',
            field=models.PositiveIntegerField(max_length=255, unique=True, null=True, verbose_name=b'C\xc3\xb3digo de barras', blank=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='price',
            field=models.FloatField(default=0, verbose_name=b'Precio \xe2\x82\xa1'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20150515_1651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='producto',
            name='bar_code',
            field=models.PositiveIntegerField(unique=True, null=True, verbose_name=b'C\xc3\xb3digo de barras', blank=True),
        ),
    ]

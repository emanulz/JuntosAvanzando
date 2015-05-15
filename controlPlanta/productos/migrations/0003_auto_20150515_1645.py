# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20150515_1630'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='familiadelproducto',
            options={'ordering': ['id'], 'verbose_name': 'Familia', 'verbose_name_plural': 'Familias'},
        ),
    ]

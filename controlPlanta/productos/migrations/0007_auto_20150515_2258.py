# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_auto_20150515_1700'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='familiadelproducto',
            options={'ordering': ['id'], 'verbose_name': 'Familia', 'verbose_name_plural': '2. Familias'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['id'], 'verbose_name': 'Producto', 'verbose_name_plural': '1. Productos'},
        ),
    ]

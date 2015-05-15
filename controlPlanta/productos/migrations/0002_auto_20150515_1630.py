# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='familiadelproducto',
            options={'verbose_name': 'Familia', 'verbose_name_plural': 'Familias'},
        ),
        migrations.AlterField(
            model_name='familiadelproducto',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name=b'nombre de la categor\xc3\xada'),
        ),
    ]

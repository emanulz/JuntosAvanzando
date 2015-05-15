# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20150515_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiadelproducto',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name=b'nombre de la familia'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='bar_code',
            field=models.PositiveIntegerField(max_length=255, unique=True, null=True, verbose_name=b'C\xc3\xb3digo de barras'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fractioned',
            field=models.BooleanField(default=0, verbose_name=b'Fracionado?'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Precio \xe2\x82\xa1'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='product_code',
            field=models.CharField(unique=True, max_length=255, verbose_name=b'C\xc3\xb3digo'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='taxes',
            field=models.BooleanField(default=0, verbose_name=b'Impuestos?'),
        ),
    ]

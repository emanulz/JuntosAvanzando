# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamiliaDelProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'nombre de la categor\xc3\xada')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_code', models.CharField(max_length=255, verbose_name=b'C\xc3\xb3digo')),
                ('bar_code', models.PositiveIntegerField(max_length=255, verbose_name=b'C\xc3\xb3digo de barras')),
                ('description', models.CharField(max_length=255, verbose_name=b'Descripci\xc3\xb3n')),
                ('price', models.PositiveIntegerField(default=0, verbose_name=b'Precio')),
                ('fractioned', models.BooleanField(default=1, verbose_name=b'Fracionado?')),
                ('taxes', models.BooleanField(default=1, verbose_name=b'Impuestos?')),
                ('taxes_amount', models.FloatField(default=0, verbose_name=b'% Impuestos', blank=True)),
                ('category', models.ForeignKey(default=1, to='productos.FamiliaDelProducto')),
            ],
        ),
    ]

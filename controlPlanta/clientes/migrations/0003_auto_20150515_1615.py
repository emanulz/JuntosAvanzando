# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_cliente_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='last_name',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Apellidos'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'Nombre'),
        ),
    ]

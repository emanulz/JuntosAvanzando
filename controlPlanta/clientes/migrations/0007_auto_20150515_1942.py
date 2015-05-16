# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20150515_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asociado',
            name='afiliate_code',
            field=models.PositiveIntegerField(verbose_name=b'N\xc3\xbamero de asociado', blank=True),
        ),
        migrations.AlterField(
            model_name='asociado',
            name='name',
            field=models.ForeignKey(verbose_name=b'Nombre', to='clientes.Cliente'),
        ),
    ]

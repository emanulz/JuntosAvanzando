# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20150515_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asociado',
            name='name',
            field=models.ForeignKey(verbose_name=b'Nombre', to='clientes.Cliente', max_length=255),
        ),
    ]

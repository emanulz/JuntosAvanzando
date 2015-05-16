# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20150515_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asociado',
            name='name',
            field=models.OneToOneField(verbose_name=b'Nombre', to='clientes.Cliente', max_length=255),
        ),
    ]

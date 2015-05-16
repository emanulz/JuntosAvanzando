# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_asociado_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='afiliate_code',
            field=models.ForeignKey(to='clientes.Asociado', null=True),
        ),
    ]

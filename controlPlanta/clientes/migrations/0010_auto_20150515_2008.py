# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_cliente_afiliate_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='EsAsociado',
            fields=[
                ('associated_number', models.PositiveIntegerField(serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='asociado',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='afiliate_code',
        ),
        migrations.AddField(
            model_name='cliente',
            name='Associated',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='associated_code',
            field=models.PositiveIntegerField(null=True, verbose_name=b'N\xc3\xbamero de asociado'),
        ),
        migrations.DeleteModel(
            name='Asociado',
        ),
        migrations.AddField(
            model_name='esasociado',
            name='name',
            field=models.OneToOneField(to='clientes.Cliente'),
        ),
    ]

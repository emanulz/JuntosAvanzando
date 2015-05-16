# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0010_auto_20150515_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='esasociado',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='Associated',
        ),
        migrations.AddField(
            model_name='cliente',
            name='associated',
            field=models.BooleanField(default=0, verbose_name=b'Es asociado?'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='associated_code',
            field=models.PositiveIntegerField(unique=True, null=True, verbose_name=b'N\xc3\xbamero de asociado'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='credit',
            field=models.BooleanField(default=0, verbose_name=b'Tiene cr\xc3\xa9dito?'),
        ),
        migrations.DeleteModel(
            name='EsAsociado',
        ),
    ]

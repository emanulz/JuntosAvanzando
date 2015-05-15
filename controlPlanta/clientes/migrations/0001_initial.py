# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import clientes.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nombre del cliente')),
                ('phone_number', models.CharField(default=clientes.models.phone_default, max_length=9, null=True, verbose_name=b'N\xc3\xbamero de tel\xc3\xa9fono', blank=True)),
                ('identification', models.CharField(max_length=255, null=True, verbose_name=b'C\xc3\xa9dula', blank=True)),
                ('adress', models.CharField(max_length=255, null=True, verbose_name=b'Direcci\xc3\xb3n', blank=True)),
                ('afiliate_code', models.PositiveIntegerField(default=0, verbose_name=b'N\xc3\xbamero de asociado', blank=True)),
                ('credit', models.BooleanField(default=0, verbose_name=b'Tiene cr\xc3\xa9dito')),
                ('credit_limit', models.FloatField(default=0, verbose_name=b'L\xc3\xadmite de cr\xc3\xa9dito', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
            ],
        ),
    ]

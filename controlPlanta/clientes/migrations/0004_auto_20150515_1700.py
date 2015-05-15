# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20150515_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asociado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('afiliate_code', models.PositiveIntegerField(default=0, verbose_name=b'N\xc3\xbamero de asociado', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='afiliate_code',
        ),
        migrations.AddField(
            model_name='asociado',
            name='name',
            field=models.ForeignKey(verbose_name=b'Nombre', to='clientes.Cliente', max_length=255),
        ),
    ]

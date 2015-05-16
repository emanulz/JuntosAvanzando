# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cajeros', '0002_auto_20150515_2309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cajero',
            options={'ordering': ['id'], 'verbose_name_plural': '1. Cajeros'},
        ),
        migrations.AlterField(
            model_name='cajero',
            name='identificatio',
            field=models.CharField(unique=True, max_length=255, verbose_name=b'C\xc3\xa9dula'),
        ),
        migrations.AlterField(
            model_name='cajero',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name=b'Apellidos'),
        ),
        migrations.AlterField(
            model_name='cajero',
            name='user',
            field=models.ForeignKey(verbose_name=b'Nombre de Usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]

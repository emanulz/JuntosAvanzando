# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cajeros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cajero',
            name='usernam',
        ),
        migrations.AddField(
            model_name='cajero',
            name='identificatio',
            field=models.CharField(default=1, unique=True, max_length=15, verbose_name=b'C\xc3\xa9dula'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cajero',
            name='user',
            field=models.ForeignKey(default=1, verbose_name=b'Nombre de Usuario', to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cajero',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name=b'Apellido'),
        ),
        migrations.AlterField(
            model_name='cajero',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'Nombre'),
        ),
    ]

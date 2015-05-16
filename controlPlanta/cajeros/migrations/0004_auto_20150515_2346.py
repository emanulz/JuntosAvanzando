# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cajeros', '0003_auto_20150515_2334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cajero',
            old_name='identificatio',
            new_name='identification',
        ),
    ]

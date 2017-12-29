# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0008_driver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='driver',
            new_name='name',
        ),
    ]

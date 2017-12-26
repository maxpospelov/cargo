# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0006_auto_20171225_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='gate',
            field=models.TextField(null=True),
        ),
    ]

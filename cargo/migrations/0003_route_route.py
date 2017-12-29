# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0002_route_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='route',
            field=models.TextField(default=''),
        ),
    ]

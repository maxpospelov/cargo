# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0003_route_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='phone',
            field=models.TextField(default=''),
        ),
    ]

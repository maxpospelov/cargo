# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0005_routestatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='status',
            field=models.ForeignKey(null=True, to='cargo.RouteStatus'),
        ),
        migrations.AlterField(
            model_name='routestatus',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0010_auto_20171229_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='driver',
            field=models.ForeignKey(to='cargo.Driver', null=True),
        ),
    ]

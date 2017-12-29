# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

ALTER_SQL = """
    ALTER TABLE cargo_route ALTER COLUMN driver TYPE integer USING driver::integer;
    """


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0009_auto_20171229_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='phone',
        ),
        migrations.RunSQL(ALTER_SQL, None, [
            migrations.AlterField(
                model_name='route',
                name='driver',
                field=models.IntegerField(),
                preserve_default=True,
            ),
        ])
    ]

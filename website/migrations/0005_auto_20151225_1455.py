# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20151225_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='pic_url',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]

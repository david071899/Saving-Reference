# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20151225_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='style',
            field=website.models.ListField(),
            preserve_default=True,
        ),
    ]

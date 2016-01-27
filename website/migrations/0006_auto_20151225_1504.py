# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20151225_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='pic_url',
            field=website.models.ListField(),
            preserve_default=True,
        ),
    ]

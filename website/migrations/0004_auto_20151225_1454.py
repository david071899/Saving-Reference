# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='pic_url',
            field=models.URLField(max_length=255),
            preserve_default=True,
        ),
    ]

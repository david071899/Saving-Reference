# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_tag_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='name',
        ),
    ]

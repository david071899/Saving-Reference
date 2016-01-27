# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='ser',
            new_name='user',
        ),
    ]

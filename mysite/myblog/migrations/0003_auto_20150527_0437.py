# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='posts',
            field=models.OneToOneField(related_name='categories', null=True, blank=True, to='myblog.Post'),
            preserve_default=True,
        ),
    ]

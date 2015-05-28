# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.AlterField(
            model_name='category',
            name='posts',
            field=models.OneToOneField(primary_key=True, default=0, serialize=False, to='myblog.Post'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rater',
            name='gender',
            field=models.CharField(default='O', max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveSmallIntegerField(),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='rating',
        ),
        migrations.AddField(
            model_name='rater',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='rater',
            field=models.ForeignKey(default=-1, to='reviews.Rater'),
            preserve_default=False,
        ),
    ]

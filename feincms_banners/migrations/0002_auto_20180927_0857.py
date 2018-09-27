# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feincms_banners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='banner',
            field=models.ForeignKey(to='feincms_banners.Banner', related_name='clicks', verbose_name='banner'),
        ),
    ]

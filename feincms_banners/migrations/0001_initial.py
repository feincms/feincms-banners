# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import feincms_banners.models
import feincms.module.medialibrary.fields


class Migration(migrations.Migration):

    dependencies = [
        ('medialibrary', '__latest__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('name', models.CharField(help_text='Only for internal use, will not be shown on the website.', max_length=100, verbose_name='name')),
                ('url', models.URLField(verbose_name='URL')),
                ('type', models.CharField(max_length=20, verbose_name='type', choices=[('skyscraper', 'skyscraper'), ('leaderboard', 'leaderboard'), ('box', 'box')])),
                ('code', models.CharField(default=feincms_banners.models.generate_key, unique=True, max_length=40, verbose_name='code')),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now, verbose_name='active from')),
                ('active_until', models.DateTimeField(null=True, verbose_name='active until', blank=True)),
                ('embeds', models.PositiveIntegerField(default=0, help_text='How many times has this banner been embdedded on a website?', verbose_name='embeds', editable=False)),
                ('impressions', models.PositiveIntegerField(default=0, help_text='How many times has an impression been registered using a Javascript callback, verifying that it actually was a browser? (Too low because of network issues and deactivated Javascript support in some browsers.)', verbose_name='impressions', editable=False)),
                ('mediafile', feincms.module.medialibrary.fields.MediaFileForeignKey(verbose_name='media file', to='medialibrary.MediaFile')),
            ],
            options={
                'ordering': ['-active_from'],
                'verbose_name': 'banner',
                'verbose_name_plural': 'banners',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='timestamp')),
                ('ip', models.IPAddressField(null=True, verbose_name='IP', blank=True)),
                ('user_agent', models.TextField(default='', verbose_name='user agent', blank=True)),
                ('referrer', models.TextField(default='', verbose_name='referrer', blank=True)),
                ('banner', models.ForeignKey(verbose_name='banner', to='feincms_banners.Banner')),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name': 'click',
                'verbose_name_plural': 'clicks',
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Banner'
        db.create_table('feincms_banners_banner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mediafile', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(to=orm['medialibrary.MediaFile'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('code', self.gf('django.db.models.fields.CharField')(default='-z0g3hknx89_h83ko8ybt2wb3s_8tdsiy9hdwpw0', unique=True, max_length=40)),
            ('active_from', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('active_until', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('embeds', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('impressions', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('feincms_banners', ['Banner'])

        # Adding model 'Click'
        db.create_table('feincms_banners_click', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('banner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='clicks', to=orm['feincms_banners.Banner'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True)),
            ('user_agent', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('referrer', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('feincms_banners', ['Click'])


    def backwards(self, orm):
        # Deleting model 'Banner'
        db.delete_table('feincms_banners_banner')

        # Deleting model 'Click'
        db.delete_table('feincms_banners_click')


    models = {
        'feincms_banners.banner': {
            'Meta': {'ordering': "['-active_from']", 'object_name': 'Banner'},
            'active_from': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'active_until': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'default': "'7u186cw9yz-nbyxc56kaua_e5elyurd7642pb14o'", 'unique': 'True', 'max_length': '40'}),
            'embeds': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impressions': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mediafile': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'to': "orm['medialibrary.MediaFile']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'feincms_banners.click': {
            'Meta': {'ordering': "['-timestamp']", 'object_name': 'Click'},
            'banner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clicks'", 'to': "orm['feincms_banners.Banner']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'referrer': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user_agent': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        },
        'medialibrary.category': {
            'Meta': {'ordering': "['parent__title', 'title']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['medialibrary.Category']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'medialibrary.mediafile': {
            'Meta': {'ordering': "['-created']", 'object_name': 'MediaFile'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['medialibrary.Category']", 'null': 'True', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        }
    }

    complete_apps = ['feincms_banners']
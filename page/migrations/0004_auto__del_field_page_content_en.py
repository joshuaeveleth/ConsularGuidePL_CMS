# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Page.content_en'
        db.delete_column(u'page_page', 'content_en')


    def backwards(self, orm):
        # Adding field 'Page.content_en'
        db.add_column(u'page_page', 'content_en',
                      self.gf('django.db.models.fields.TextField')(default='rererer'),
                      keep_default=False)


    models = {
        u'page.page': {
            'Meta': {'object_name': 'Page'},
            'additional_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'additional_pl': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_pl': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 1, 8, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 1, 8, 0, 0)'}),
            'page_type': ('django.db.models.fields.CharField', [], {'default': "'text'", 'max_length': '4'}),
            'parent_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_page'", 'null': 'True', 'to': u"orm['page.Page']"}),
            'place': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'title_pl': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'version': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'zoom': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['page']
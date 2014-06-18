# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Video.title_en'
        db.alter_column(u'video_video', 'title_en', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Video.title_pl'
        db.alter_column(u'video_video', 'title_pl', self.gf('django.db.models.fields.CharField')(max_length=40))

    def backwards(self, orm):

        # Changing field 'Video.title_en'
        db.alter_column(u'video_video', 'title_en', self.gf('django.db.models.fields.CharField')(max_length=80))

        # Changing field 'Video.title_pl'
        db.alter_column(u'video_video', 'title_pl', self.gf('django.db.models.fields.CharField')(max_length=80))

    models = {
        u'video.video': {
            'Meta': {'object_name': 'Video'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'conversion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'poster_time': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'sync_status': ('django.db.models.fields.CharField', [], {'default': "'waiting'", 'max_length': '16'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'title_pl': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'video_android1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_android2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_android3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_ios1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_ios2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_ios3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_ios_variant': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_original': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_type': ('django.db.models.fields.CharField', [], {'default': "u'LC'", 'max_length': '2'}),
            'views': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['video']
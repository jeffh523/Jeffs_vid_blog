# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.videoURL'
        db.add_column(u'Blog_post', 'videoURL',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=80),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.videoURL'
        db.delete_column(u'Blog_post', 'videoURL')


    models = {
        u'Blog.post': {
            'Meta': {'object_name': 'Post'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'dateCreated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'videoURL': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['Blog']
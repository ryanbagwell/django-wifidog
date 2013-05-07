# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WIFIPing'
        db.create_table('wifiauth_wifiping', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gw_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sys_uptime', self.gf('django.db.models.fields.IntegerField')()),
            ('sys_memfree', self.gf('django.db.models.fields.IntegerField')()),
            ('wifidog_uptime', self.gf('django.db.models.fields.IntegerField')()),
            ('sys_load', self.gf('django.db.models.fields.FloatField')()),
            ('ping_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('wifiauth', ['WIFIPing'])

        # Adding model 'WIFIAuthRequest'
        db.create_table('wifiauth_wifiauthrequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stage', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('mac', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('incoming', self.gf('django.db.models.fields.IntegerField')()),
            ('outgoing', self.gf('django.db.models.fields.IntegerField')()),
            ('result', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('wifiauth', ['WIFIAuthRequest'])


    def backwards(self, orm):
        # Deleting model 'WIFIPing'
        db.delete_table('wifiauth_wifiping')

        # Deleting model 'WIFIAuthRequest'
        db.delete_table('wifiauth_wifiauthrequest')


    models = {
        'wifiauth.wifiauthrequest': {
            'Meta': {'object_name': 'WIFIAuthRequest'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incoming': ('django.db.models.fields.IntegerField', [], {}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'outgoing': ('django.db.models.fields.IntegerField', [], {}),
            'result': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'stage': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'wifiauth.wifiping': {
            'Meta': {'object_name': 'WIFIPing'},
            'gw_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ping_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'sys_load': ('django.db.models.fields.FloatField', [], {}),
            'sys_memfree': ('django.db.models.fields.IntegerField', [], {}),
            'sys_uptime': ('django.db.models.fields.IntegerField', [], {}),
            'wifidog_uptime': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['wifiauth']
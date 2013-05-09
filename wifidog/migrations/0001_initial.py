# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WIFIPing'
        db.create_table('wifidog_wifiping', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gw_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sys_uptime', self.gf('django.db.models.fields.IntegerField')()),
            ('sys_memfree', self.gf('django.db.models.fields.IntegerField')()),
            ('wifidog_uptime', self.gf('django.db.models.fields.IntegerField')()),
            ('sys_load', self.gf('django.db.models.fields.FloatField')()),
            ('ping_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('wifidog', ['WIFIPing'])

        # Adding model 'WIFIAuthRequest'
        db.create_table('wifidog_wifiauthrequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='auth_requests', null=True, to=orm['auth.User'])),
            ('stage', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('mac', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('incoming', self.gf('django.db.models.fields.IntegerField')()),
            ('outgoing', self.gf('django.db.models.fields.IntegerField')()),
            ('result', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('request_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('wifidog', ['WIFIAuthRequest'])

        # Adding model 'Token'
        db.create_table('wifidog_token', (
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tokens', primary_key=True, to=orm['auth.User'])),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('expires', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('wifidog', ['Token'])


    def backwards(self, orm):
        # Deleting model 'WIFIPing'
        db.delete_table('wifidog_wifiping')

        # Deleting model 'WIFIAuthRequest'
        db.delete_table('wifidog_wifiauthrequest')

        # Deleting model 'Token'
        db.delete_table('wifidog_token')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'wifidog.token': {
            'Meta': {'object_name': 'Token'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'expires': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tokens'", 'primary_key': 'True', 'to': "orm['auth.User']"})
        },
        'wifidog.wifiauthrequest': {
            'Meta': {'object_name': 'WIFIAuthRequest'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incoming': ('django.db.models.fields.IntegerField', [], {}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'outgoing': ('django.db.models.fields.IntegerField', [], {}),
            'request_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'result': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'stage': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'auth_requests'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'wifidog.wifiping': {
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

    complete_apps = ['wifidog']
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Cuenta.identificador'
        db.add_column(u'backend_cuenta', 'identificador',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Alumno'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Cuenta.identificador'
        db.delete_column(u'backend_cuenta', 'identificador_id')


    models = {
        u'backend.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'ap_materno': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ap_paterno': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'contrasena': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'encriptado': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fecha_alta': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matricula': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'nombre1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nombre2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'backend.camion': {
            'Meta': {'object_name': 'Camion'},
            'asientos': ('django.db.models.fields.IntegerField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'placa': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'velocidad': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'backend.cobro': {
            'Meta': {'object_name': 'Cobro'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'max_length': '7'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'backend.cuenta': {
            'Meta': {'object_name': 'Cuenta'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Alumno']", 'null': 'True', 'blank': 'True'}),
            'saldo': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'tipoServicio': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'backend.deposito': {
            'Meta': {'object_name': 'Deposito'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'fechaDeposito': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'backend.registroentrada': {
            'Meta': {'object_name': 'RegistroEntrada'},
            'fechaIn': ('django.db.models.fields.DateField', [], {}),
            'horaOut': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Alumno']"}),
            'latitud': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'backend.registrosalida': {
            'Meta': {'object_name': 'RegistroSalida'},
            'fechaOut': ('django.db.models.fields.DateField', [], {}),
            'horaOut': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Alumno']"}),
            'latitud': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'backend.ruta': {
            'Meta': {'object_name': 'Ruta'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kilometraje': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'llegada': ('django.db.models.fields.TimeField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'salida': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['backend']
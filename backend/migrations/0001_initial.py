# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Alumno'
        db.create_table(u'backend_alumno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre1', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('nombre2', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('ap_paterno', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('ap_materno', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('matricula', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('fecha_alta', self.gf('django.db.models.fields.DateField')()),
            ('contrasena', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('encriptado', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'backend', ['Alumno'])

        # Adding model 'Ruta'
        db.create_table(u'backend_ruta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('salida', self.gf('django.db.models.fields.TimeField')()),
            ('llegada', self.gf('django.db.models.fields.TimeField')()),
            ('kilometraje', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
        ))
        db.send_create_signal(u'backend', ['Ruta'])

        # Adding model 'RegistroSalida'
        db.create_table(u'backend_registrosalida', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identificador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Alumno'])),
            ('fechaOut', self.gf('django.db.models.fields.DateField')()),
            ('horaOut', self.gf('django.db.models.fields.TimeField')()),
            ('latitud', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('longitud', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'backend', ['RegistroSalida'])

        # Adding model 'RegistroEntrada'
        db.create_table(u'backend_registroentrada', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identificador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Alumno'])),
            ('fechaIn', self.gf('django.db.models.fields.DateField')()),
            ('horaOut', self.gf('django.db.models.fields.TimeField')()),
            ('latitud', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('longitud', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'backend', ['RegistroEntrada'])

        # Adding model 'Camion'
        db.create_table(u'backend_camion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('latitud', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('longitud', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('velocidad', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('placa', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('asientos', self.gf('django.db.models.fields.IntegerField')(max_length=60)),
        ))
        db.send_create_signal(u'backend', ['Camion'])

        # Adding model 'Cobro'
        db.create_table(u'backend_cobro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')(max_length=7)),
        ))
        db.send_create_signal(u'backend', ['Cobro'])

        # Adding model 'Cuenta'
        db.create_table(u'backend_cuenta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipoServicio', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('saldo', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
        ))
        db.send_create_signal(u'backend', ['Cuenta'])

        # Adding model 'Deposito'
        db.create_table(u'backend_deposito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('fechaDeposito', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'backend', ['Deposito'])


    def backwards(self, orm):
        # Deleting model 'Alumno'
        db.delete_table(u'backend_alumno')

        # Deleting model 'Ruta'
        db.delete_table(u'backend_ruta')

        # Deleting model 'RegistroSalida'
        db.delete_table(u'backend_registrosalida')

        # Deleting model 'RegistroEntrada'
        db.delete_table(u'backend_registroentrada')

        # Deleting model 'Camion'
        db.delete_table(u'backend_camion')

        # Deleting model 'Cobro'
        db.delete_table(u'backend_cobro')

        # Deleting model 'Cuenta'
        db.delete_table(u'backend_cuenta')

        # Deleting model 'Deposito'
        db.delete_table(u'backend_deposito')


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
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Nivel'
        db.create_table(u'configuracion_nivel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'configuracion', ['Nivel'])

        # Adding model 'Grado'
        db.create_table(u'configuracion_grado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('nivel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configuracion.Nivel'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'configuracion', ['Grado'])

        # Adding model 'Seccion'
        db.create_table(u'configuracion_seccion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'configuracion', ['Seccion'])

        # Adding model 'Grupo'
        db.create_table(u'configuracion_grupo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('nivel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configuracion.Nivel'])),
            ('grado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configuracion.Grado'])),
            ('seccion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configuracion.Seccion'])),
            ('maximo', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('numalumnos', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'configuracion', ['Grupo'])

        # Adding model 'Maestro'
        db.create_table(u'configuracion_maestro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('fechanacimiento', self.gf('django.db.models.fields.DateField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=50)),
            ('rfc', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('curp', self.gf('django.db.models.fields.CharField')(max_length=22, null=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('celualr', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('colonia', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('cp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('carrera', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('maestria', self.gf('django.db.models.fields.CharField')(default='No', max_length=2)),
            ('doctorado', self.gf('django.db.models.fields.CharField')(default='No', max_length=2)),
            ('estadocivil', self.gf('django.db.models.fields.CharField')(default='Soltero', max_length=15)),
        ))
        db.send_create_signal(u'configuracion', ['Maestro'])

        # Adding M2M table for field nivel on 'Maestro'
        m2m_table_name = db.shorten_name(u'configuracion_maestro_nivel')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('maestro', models.ForeignKey(orm[u'configuracion.maestro'], null=False)),
            ('nivel', models.ForeignKey(orm[u'configuracion.nivel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['maestro_id', 'nivel_id'])

        # Adding model 'Padre'
        db.create_table(u'configuracion_padre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default='Padre', max_length=5)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=50)),
            ('nivelestudios', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('ocupacio', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('curp', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('fechanacimento', self.gf('django.db.models.fields.DateField')()),
            ('rfc', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('domicilio', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('colonia', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('nomemp', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('domcilioemp', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('colemp', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('telemp', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('telcasa', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('movil', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'configuracion', ['Padre'])

        # Adding model 'MaestroxGpo'
        db.create_table(u'configuracion_maestroxgpo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('nivel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configuracion.Nivel'])),
            ('materia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Materia'], unique=True)),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configuracion.Grupo'])),
            ('maestro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configuracion.Maestro'])),
        ))
        db.send_create_signal(u'configuracion', ['MaestroxGpo'])


    def backwards(self, orm):
        # Deleting model 'Nivel'
        db.delete_table(u'configuracion_nivel')

        # Deleting model 'Grado'
        db.delete_table(u'configuracion_grado')

        # Deleting model 'Seccion'
        db.delete_table(u'configuracion_seccion')

        # Deleting model 'Grupo'
        db.delete_table(u'configuracion_grupo')

        # Deleting model 'Maestro'
        db.delete_table(u'configuracion_maestro')

        # Removing M2M table for field nivel on 'Maestro'
        db.delete_table(db.shorten_name(u'configuracion_maestro_nivel'))

        # Deleting model 'Padre'
        db.delete_table(u'configuracion_padre')

        # Deleting model 'MaestroxGpo'
        db.delete_table(u'configuracion_maestroxgpo')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'configuracion.grado': {
            'Meta': {'object_name': 'Grado'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nivel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Nivel']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'configuracion.grupo': {
            'Meta': {'object_name': 'Grupo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'grado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Grado']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maximo': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nivel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Nivel']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'numalumnos': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'seccion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Seccion']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'configuracion.maestro': {
            'Meta': {'object_name': 'Maestro'},
            'carrera': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'celualr': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'cp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'curp': ('django.db.models.fields.CharField', [], {'max_length': '22', 'null': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'doctorado': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '50'}),
            'estadocivil': ('django.db.models.fields.CharField', [], {'default': "'Soltero'", 'max_length': '15'}),
            'fechanacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maestria': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '2'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nivel': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Nivel']", 'symmetrical': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'configuracion.maestroxgpo': {
            'Meta': {'object_name': 'MaestroxGpo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Grupo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maestro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Maestro']"}),
            'materia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Materia']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nivel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Nivel']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'configuracion.nivel': {
            'Meta': {'object_name': 'Nivel'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'configuracion.padre': {
            'Meta': {'object_name': 'Padre'},
            'colemp': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'curp': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'domcilioemp': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'domicilio': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '50'}),
            'fechanacimento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'movil': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'nivelestudios': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nomemp': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'ocupacio': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'telcasa': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'telemp': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "'Padre'", 'max_length': '5'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'configuracion.seccion': {
            'Meta': {'object_name': 'Seccion'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'principal.materia': {
            'Meta': {'object_name': 'Materia'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['configuracion.Grupo']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nivel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Nivel']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['configuracion']
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field grupo on 'Materia'
        db.delete_table(db.shorten_name(u'principal_materia_grupo'))

        # Adding M2M table for field grado on 'Materia'
        m2m_table_name = db.shorten_name(u'principal_materia_grado')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('materia', models.ForeignKey(orm[u'principal.materia'], null=False)),
            ('grado', models.ForeignKey(orm[u'configuracion.grado'], null=False))
        ))
        db.create_unique(m2m_table_name, ['materia_id', 'grado_id'])


    def backwards(self, orm):
        # Adding M2M table for field grupo on 'Materia'
        m2m_table_name = db.shorten_name(u'principal_materia_grupo')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('materia', models.ForeignKey(orm[u'principal.materia'], null=False)),
            ('grupo', models.ForeignKey(orm[u'configuracion.grupo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['materia_id', 'grupo_id'])

        # Removing M2M table for field grado on 'Materia'
        db.delete_table(db.shorten_name(u'principal_materia_grado'))


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
        u'principal.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'celualr': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'cp': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'curp': ('django.db.models.fields.CharField', [], {'max_length': '22', 'null': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'fechanacimiento': ('django.db.models.fields.DateField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Grupo']", 'null': 'True', 'blank': 'True'}),
            'hermanos': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nivel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Nivel']", 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'padre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Padre']", 'null': 'True', 'blank': 'True'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'principal.calificacion': {
            'Meta': {'object_name': 'Calificacion'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Alumno']"}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Materia']"}),
            'mes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Mes']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'principal.cicloescolar': {
            'Meta': {'object_name': 'Cicloescolar'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'fechafin': ('django.db.models.fields.DateField', [], {}),
            'fechaini': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'principal.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'principal.materia': {
            'Meta': {'object_name': 'Materia'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'grado': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['configuracion.Grado']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nivel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Nivel']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'principal.materiaxgrupo': {
            'Meta': {'object_name': 'MateriaxGrupo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Grupo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Materia']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nivel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Nivel']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'principal.mes': {
            'Meta': {'object_name': 'Mes'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['principal']
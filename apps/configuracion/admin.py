from django.contrib import admin

from .models import Nivel, Grupo, Grado, Maestro,Padre,Seccion,MaestroxGpo

class MaestroxGpoAdmin(admin.ModelAdmin):
	list_display = ('nivel','materia','grupo','maestro',)
	list_filter = ('nivel','materia','grupo','maestro',)

class GrupoAdmin(admin.ModelAdmin):
	list_display = ('nombre','nivel','grado','seccion','maximo','numalumnos',)
	list_filter = ('nombre','nivel','grado','seccion','maximo','numalumnos',)

class MaestroAdmin(admin.ModelAdmin):
	list_display = ('nombre','telefono','celualr',)
	filter_horizontal = ('nivel',)
	list_filter = ('nombre','nivel',)
	search_fields = ('nombre',)
 

admin.site.register(Nivel)
admin.site.register(Grupo,GrupoAdmin)
admin.site.register(Grado)
admin.site.register(Maestro,MaestroAdmin)
admin.site.register(Padre)
admin.site.register(Seccion)
admin.site.register(MaestroxGpo,MaestroxGpoAdmin)
 

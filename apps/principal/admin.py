from django.contrib import admin

from .models import Empresa,Alumno,Mes,Materia,Calificacion,MateriaxGrupo,Cicloescolar

class MateriaxGrupoAdmin(admin.ModelAdmin):
	list_display = ('id','nivel','materia','grupo','status',)
	list_filter = ('nivel','materia','grupo','status',)
	search_fields = ('materia__materia',)
	list_editable = ('nivel','materia','grupo','status',)
	raw_id_fields = ('materia','grupo',)

class MateriaAdmin(admin.ModelAdmin):
	list_display =('materia','nivel','grado',)
	list_filter = ('materia', 'nivel','grado',)
	search_fields = ('materia__materia',)

class CicloescolarAdmin(admin.ModelAdmin):
	list_display=('descripcion','fechaini','fechafin',)


admin.site.register(Empresa)
admin.site.register(Alumno)
admin.site.register(Mes)
admin.site.register(Materia,MateriaAdmin)
admin.site.register(Calificacion)
admin.site.register(MateriaxGrupo,MateriaxGrupoAdmin)
admin.site.register(Cicloescolar,CicloescolarAdmin)



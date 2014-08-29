from django.contrib import admin

from .models import Transporte, AlumnoTrasp,Conducta

class TransporteAdmin(admin.ModelAdmin):
	list_display = ('mes','servicio','costo','fechalimitepago','penaliza')
	list_filter = ('mes','servicio')

class AlumnoTraspAdmin(admin.ModelAdmin):
	list_display = ('alumno','transporte','recojerEn','entregarEn')
	list_filter =('alumno','pagado')

class ConductaAdmin(admin.ModelAdmin):
	list_display = ('alumno','maestro','comentario','fecha')

 
admin.site.register(Transporte,TransporteAdmin)
admin.site.register(AlumnoTrasp,AlumnoTraspAdmin)
admin.site.register(Conducta,ConductaAdmin)

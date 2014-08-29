from django.contrib import admin
from apps.maestro.models import Asistencia


class AsistenciaAdmin(admin.ModelAdmin):
	list_display = ('alumno','falta','fecha')

admin.site.register(Asistencia,AsistenciaAdmin)

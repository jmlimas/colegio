from django.contrib import admin
from views import ConceptoCobro,Banco,BecaAlumno,Cobranza


# Register your models here.

class ConceptoCobroAdmin(admin.ModelAdmin):
	list_display = ('nombre','nivel','importe','fechaLimitePago','penaliza')
	list_filter = ('nombre','nivel')

class BancoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	list_filter = ('nombre',)

class BecaAlumnoAdmin(admin.ModelAdmin):
	list_display = ('alumno','porcentaje',)
	list_filter = ('alumno','porcentaje',) 

class CobranzaAdmin(admin.ModelAdmin):
	list_display = ('alumno','concepto','pagado')
	list_filter = ('alumno','pagado',)



 


admin.site.register(ConceptoCobro,ConceptoCobroAdmin)
admin.site.register(Banco,BancoAdmin)
admin.site.register(BecaAlumno,BecaAlumnoAdmin)
admin.site.register(Cobranza,CobranzaAdmin)
from django.db import models
from apps.configuracion.models import TimeStampModel


class Transporte(TimeStampModel):
	Op = (
		('Parcial', 'Parcial'),
		('Completo', 'Completo'),
	)

	Op2 = (
			('Si', 'Si'),
			('No', 'No'),
		)

	mes = models.ForeignKey('principal.Mes')
	servicio = models.CharField(max_length=8,choices=Op)
	costo = models.DecimalField(max_digits=6,decimal_places=2,default=0)
	fechalimitepago = models.DateField()
	penaliza =  models.CharField(max_length=2,choices=Op2)	
 
	def __unicode__(self):
		 return unicode(self.servicio)


class AlumnoTrasp(TimeStampModel):
	Op2 = (
			('Si', 'Si'),
			('No', 'No'),
		)
	
	alumno = models.ForeignKey('principal.Alumno')
	transporte = models.ForeignKey('Transporte')
	recojerEn = models.CharField(max_length=140, null=True, blank=True)
	entregarEn = models.CharField(max_length=140, null=True, blank=True)
	pagado = models.CharField(max_length=2,choices=Op2)

	def __unicode__(self):
		return unicode(self.alumno)	 
     

 
class Conducta(TimeStampModel):
	alumno = models.ForeignKey('principal.Alumno')
	maestro = models.ForeignKey('configuracion.Maestro')
	comentario = models.TextField(max_length=1500,null=True)
	fecha = models.DateField()

	def __unicode__(self):
		return unicode(self.alumno)


 


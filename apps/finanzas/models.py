from django.db import models
from apps.configuracion.models import TimeStampModel
 

class ConceptoCobro(TimeStampModel):
	Op = (
		('No', 'No'),
		('Si', 'Si'),
	)

	nombre = models.CharField(max_length=80)	 
	nivel = models.ForeignKey('configuracion.Nivel',null=True, blank=True)
	importe =  models.DecimalField(max_digits=8,decimal_places=2,default=0)
	fechaLimitePago = models.DateField(null=True)
	penaliza =  models.CharField(max_length=2,choices=Op,default='No',null=True)
	importeMulta = models.DecimalField(max_digits=6,decimal_places=2,default=0)
	
	def __unicode__(self):
		return self.nombre


class Banco(TimeStampModel):
	nombre = models.CharField(max_length=30)
	convenio = models.IntegerField()

	def __unicode__(self):
		return self.nombre


class BecaAlumno(TimeStampModel):
	alumno = models.ForeignKey('principal.alumno',unique=True)
	porcentaje = models.IntegerField(default=0)
	
	def __unicode__(self):
		return unicode(self.alumno)	 
		 


class Cobranza(TimeStampModel):
	Op = (
		('Banco', 'Banco'),
		('Caja', 'Caja'),
	)
	alumno = models.ForeignKey('principal.Alumno')	
	concepto = models.ForeignKey('ConceptoCobro')
	beca = models.ForeignKey('BecaAlumno', null=True,blank=True)
	recargo = models.DecimalField(max_digits=8,decimal_places=2,default=0)
	tipopago = models.CharField(max_length=5, choices=Op, null=True,blank=True)
	referencia = models.CharField(max_length=30, null=True,blank=True)
	banco = models.ForeignKey('banco', null=True,blank=True)
	numCorte = models.IntegerField(null=True,blank=True)	
	totalapagar = models.DecimalField(max_digits=8,decimal_places=2,default=0)
	fechaCorte = models.DateField(null=True,blank=True)
	fechapago = models.DateTimeField(null=True,blank=True)
	pagado = models.BooleanField(default=False)

	def __unicode__(self):
		ctalmno = "%s" % (self.alumno) 
		return ctalmno

	class Meta:
		ordering = ["totalapagar"]

	


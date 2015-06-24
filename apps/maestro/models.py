from django.db import models
from apps.configuracion.models import TimeStampModel
from apps.principal.models import Alumno
from datetime import datetime 

class Asistencia(TimeStampModel):
	Op = (
		('A', 'A'),
		('R', 'R'),
		('F', 'F'),
	)

	alumno = models.ForeignKey(Alumno)
	falta = models.CharField(max_length=1, choices=Op, default ='A') 
	fecha = models.DateField(default=datetime.now)
	 

	class Meta:
		unique_together = ("alumno", "fecha")


	def __unicode__(self):
		return unicode(self.alumno.nombre) 


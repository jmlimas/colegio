from django.db import models
from apps.configuracion.models import TimeStampModel

class Empresa(TimeStampModel):
	nombre = models.CharField(max_length=250)
	direccion = models.CharField(max_length=150)
	telefono = models.CharField(max_length=25)
	rfc = models.CharField(max_length=13)
	email = models.EmailField(max_length=50,unique=True)

	def __unicode__(self):
		return self.nombre


class Alumno(TimeStampModel):
	Sex = (
        ('M', 'Mujer'),
        ('H', 'Hombre'),
    )

	Op = (
		('No', 'No'),
		('Si', 'Si'),
	)
	#matricula = models.CharField(max_length=6)
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=120)
	foto 	  = models.ImageField(upload_to='alumno',null=True,blank=True)
	fechanacimiento = models.DateField()
	rfc = models.CharField(max_length=15,null=True)
  	curp = models.CharField(max_length=22,null=True)
	sexo = models.CharField("Sex",max_length=1, choices=Sex,null=True) 
	hermanos = models.CharField(max_length=2,choices=Op,default='No')
	direccion = models.CharField(max_length=140,null=True)
  	colonia = models.CharField(max_length=80,null=True)
  	telefono = models.CharField(max_length=12,null=True)
  	celualr = models.CharField(max_length=12,null=True)
  	cp = models.IntegerField(default=0 ,null=True)
  	ciudad = models.CharField(max_length=60 ,null=True)		 
	estado =  models.CharField(max_length=60,null=True)	
	email = models.EmailField(max_length=50,unique=True,null=True)
	nivel = models.ForeignKey('configuracion.Nivel',null=True, blank=True)
	grupo = models.ForeignKey('configuracion.Grupo', null=True, blank=True)
	padre = models.ForeignKey('configuracion.Padre',null=True, blank=True)
	contacto = models.CharField(max_length=150,null=True, blank=True)

	
	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombre,self.apellidos)
		return nombreCompleto


class Materia(TimeStampModel):
	materia = models.CharField(max_length=150)
	nivel = models.ForeignKey('configuracion.Nivel', null=True, blank=True)
	grado = models.ForeignKey('configuracion.Grado',null=True, blank=True)

	class Meta:
		ordering = ["materia","grado"]
	 
	
  	def __unicode__(self):
  		return self.materia


class Mes(TimeStampModel):
	nombre = models.CharField(max_length=12)

	def __unicode__(self):
		return self.nombre		


class Calificacion(TimeStampModel):
	alumno = models.ForeignKey('Alumno')
	materia = models.ForeignKey('Materia')
	mes = models.ForeignKey('Mes')
	#calificacion = models.DecimalField(max_digits=2, decimal_places=2,default=0)
	calificacion = models.IntegerField()

	def __unicode__(self):
		return self.alumno
		

#asigna materias por grupo	 
class MateriaxGrupo(TimeStampModel):
	nivel = models.ForeignKey('configuracion.Nivel')
	materia = models.ForeignKey('Materia')
	grupo = models.ForeignKey('configuracion.Grupo')
	status = models.BooleanField(default=False)

	def __unicode__(self):
		materiaxgpo = "%s %s %s"%(self.materia.materia,self.nivel.Nombre,self.grupo.nombre)
		return materiaxgpo
		

class Cicloescolar(TimeStampModel):
	descripcion = models.CharField(max_length=80)
	fechaini = models.DateField()
	fechafin = models.DateField()

	def __unicode__(self):
		return self.descripcion

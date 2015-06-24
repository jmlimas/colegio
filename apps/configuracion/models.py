from django.db import models
#from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



class TimeStampModel(models.Model):

	user        = models.ForeignKey(User,null=True, blank=True, db_index=True)
	created     = models.DateTimeField(auto_now_add=True)
	modified    = models.DateTimeField(auto_now=True) 

	class Meta:
		abstract = True


class Nivel(TimeStampModel):
	Nombre = models.CharField(max_length=60)
    
	def __unicode__(self):
		return self.Nombre

class Grado(TimeStampModel):	
	nivel  = models.ForeignKey('Nivel')
	nombre = models.CharField(max_length=1)
	
	def __unicode__(self):
		nivelgrado = "%s %s " % (self.nivel,self.nombre)
		return nivelgrado

class Seccion(TimeStampModel):
	nombre =models.CharField(max_length=1)

	def __unicode__(self):
		return self.nombre


class Grupo(TimeStampModel):
	nombre = models.CharField(max_length=60)
	nivel  = models.ForeignKey('Nivel')
	grado  = models.ForeignKey('Grado')
	seccion = models.ForeignKey('Seccion')
	maximo = models.IntegerField(default=0,validators=[MinValueValidator(1),
                                       MaxValueValidator(60)]) 
	numalumnos = models.IntegerField(default=0,null=True, blank=True)

	def cupo(self):
			return self.maximo - self.numalumnos

	class Meta:
		ordering = ["nivel","nombre"]


	def __unicode__(self):
		gruponivel = "%s %s %s" % (self.nombre,self.seccion,self.nivel)
		return gruponivel

	

class Maestro(TimeStampModel):

	Sex = (
        ('M', 'Mujer'),
        ('H', 'Hombre'),
    )

	Op = (
		('No', 'No'),
		('Si', 'Si'),
	)

	Civil=(
		('Soltero','Soltero'),
		('Casado', 'Casado'),
		('Divorciado','Divorciado'),
		('Union Libre','Union Libre'),
		('Separado','Separado'),
	)

 	nombre = models.CharField(max_length=200)
 	sexo = models.CharField("Sex",max_length=1, choices=Sex) 	 
  	fechanacimiento = models.DateField()
  	email = models.EmailField(max_length=50,unique=True)
  	rfc = models.CharField(max_length=15)
  	curp = models.CharField(max_length=22,null=True)
  	telefono = models.CharField(max_length=20)
  	celualr = models.CharField(max_length=12)
  	direccion = models.CharField(max_length=140)
  	colonia = models.CharField(max_length=80)
  	cp = models.IntegerField(default=0)
  	carrera = models.CharField(max_length=140)
  	maestria = models.CharField(max_length=2,choices=Op,default='No')
  	doctorado = models.CharField(max_length=2,choices=Op,default='No')
  	estadocivil = models.CharField(max_length=15,choices=Civil,default='Soltero')
  	nivel = models.ManyToManyField('Nivel')
  	

  	def __unicode__(self):
  		return self.nombre


class Padre(TimeStampModel):
	Op = (
		('Padre', 'Padre'),
		('Madre', 'Madre'),
		('Tutor', 'Tutor'),
	)
	tipo = models.CharField(max_length=5,choices=Op,default='Padre')
	nombre = models.CharField(max_length=200)
	email = models.EmailField(max_length=50,unique=True)
	nivelestudios = models.CharField(max_length=140)
	ocupacio = models.CharField(max_length=140)
	curp = models.CharField(max_length=20,null=True)
	fechanacimento = models.DateField()
	rfc = models.CharField(max_length=15,null=True)
	domicilio = models.CharField(max_length=80)
	colonia  = models.CharField(max_length=60)
	nomemp = models.CharField(max_length=140)
	domcilioemp = models.CharField(max_length=80)
	colemp = models.CharField(max_length=60)
	telemp = models.CharField(max_length=10)
	telcasa = models.CharField(max_length=10)
	movil = models.CharField(max_length=10)
	
	def __unicode__(self):
		 return self.nombre
		 

class MaestroxGpo(TimeStampModel):
	nivel = models.ForeignKey('Nivel')
	materia = models.ForeignKey('principal.Materia')
	grupo = models.ForeignKey('Grupo')
	maestro = models.ForeignKey('Maestro')

def __unicode__(self):
		maestroxgpo = "%s %s %s" % (self.nivel,self.materia,self.grupo)
		return maestroxgpo


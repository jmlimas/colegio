from django import forms
from models import Alumno, Calificacion, Empresa, Materia,MateriaxGrupo,Cicloescolar


class AddAlumnoForm(forms.ModelForm):
	class Meta:
		model = Alumno
		exclude = ['user']

class AddCicloForm(forms.ModelForm):
	class Meta:
		model = Cicloescolar
		exclude = ['user']
		
class AddCalForm(forms.ModelForm):
	class Meta:
		model = Calificacion
		exclude = ['user']

class AddEmpresaForm(forms.ModelForm):
	class Meta :
		model = Empresa
		exclude = ['user']

class AddMateriaForm(forms.ModelForm):
	class Meta:
		model = Materia 
		exclude = ['user']
		
class AddMateriaxGrupoForm(forms.ModelForm):
	class Meta:
		model = MateriaxGrupo
		exclude = ['user']
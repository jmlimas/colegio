from django import forms
from models import Nivel,Grado,Grupo,Maestro,Padre,Seccion,MaestroxGpo

class AddNivelForm(forms.ModelForm):
	class Meta:
		model = Nivel

class AddGradoForm(forms.ModelForm):
	class Meta:
		model = Grado
		#fields = ('nivel','nombre',)
		exclude = ['user']

class AddGrupoForm(forms.ModelForm):
	class Meta:
		model = Grupo
		exclude = ['numalumnos','user']  

	widgets = {
    'maximo': forms.NumberInput(attrs={
    	'class' : 'cajas',
    	'id' : 'id_maximo',
    	'min': '1', 'max': '60'})
    }
		 

class AddMaestroForm(forms.ModelForm):
	class Meta:
		model = Maestro
		exclude = ['user']

class AddPadreForm(forms.ModelForm):
	class Meta:
		model = Padre
		exclude = ['user']

class AddSeccionForm(forms.ModelForm):
	nombre = forms.RegexField(regex=r'^[a-zA-Z]+$',
	help_text = "Nombre de Seccion eje A",error_message = "Bebes ingresar solo letras y espacios")
	class Meta:
		model = Seccion
		fields = ['nombre',]

class MaestroxGpoForm(forms.ModelForm):
	class Meta:
		model = MaestroxGpo
		exclude= ['user']
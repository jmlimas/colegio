from django import forms
from models import Transporte,AlumnoTrasp,Conducta


class AddTransporteForm(forms.ModelForm):
	fechalimitepago = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'yyyy-mm-dd','required': 'true'}))

	class Meta:
		model = Transporte
		exclude = ['user']

class AddAlumnoTraspForm(forms.ModelForm):
	recojerEn = forms.CharField(widget=forms.Textarea(attrs={'rows':'1', 'cols': '80'})) 
	entregarEn =  forms.CharField(widget=forms.Textarea(attrs={'rows':'1', 'cols': '80'}))
	class Meta:
		model = AlumnoTrasp
		exclude = ['user'] 

class AddConductaForm(forms.ModelForm):
	comentario = forms.CharField(widget = forms.Textarea(attrs={'rows':'4', 'cols':'50'}))
	class Meta:
		model = Conducta
		exclude = ['user']
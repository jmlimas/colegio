from django import forms
from models import Asistencia

class AddAsistenciaForm(forms.ModelForm):
	class Meta:
		model = Asistencia
		exclude = ['user']

from django import forms
from .models import ConceptoCobro,Banco,BecaAlumno

class AddConceptoForm(forms.ModelForm):
	class Meta:
		model = ConceptoCobro
		exclude = ['user']

class AddBancoForm(forms.ModelForm):
	class Meta:
		model = Banco
		exclude = ['user']

class AddBecaAlumnoForm(forms.ModelForm):
	class Meta:
		model = BecaAlumno
		exclude = ['user']

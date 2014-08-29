from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,TemplateView
from .models import ConceptoCobro, Banco,Cobranza,BecaAlumno
from .forms import AddConceptoForm,AddBancoForm,AddBecaAlumnoForm
from apps.principal.models import Alumno
from django.core.urlresolvers import reverse
from datetime import date
from decimal import Decimal


class AddConcepto(CreateView):
	form_class = AddConceptoForm
	template_name  = 'finanzas/conceptocobro_form.html'
	success_url = '/listconceptos'

class ListConceptos(ListView):
	context_object_name ='conceptos'
	model = ConceptoCobro

class UpdateConceptos(UpdateView):
	form_class = AddConceptoForm
	model = ConceptoCobro
	def get_success_url(self):
		return reverse('finanzas:list_conceptos')

class AddBancos(CreateView):
	form_class=AddBancoForm
	template_name='finanzas/banco_form.html'
	success_url = '/listbancos'

class ListBancos(ListView):
	context_object_name ='bancos'
	model = Banco

class UpdateBancos(UpdateView):
	form_class = AddBancoForm
	model = Banco
	def get_success_url(self):
		return reverse('finanzas:list_bancos')

class AddBecaAlumno(CreateView):
	form_class = AddBecaAlumnoForm
	template_name = 'finanzas/becaalumno_form.html'
	success_url = '/'

class ListBecaAlumno(ListView):
	context_object_name = 'beca'
	model = BecaAlumno

class UpdateBeca(UpdateView):
	form_class = AddBecaAlumnoForm
	model = BecaAlumno

	def get_success_url(self):
		return reverse('finanzas:list_becaalumno')


class ListCobranza(TemplateView):
	template_name = 'finanzas/cobranza_list.html' 

 
	def post(self, request, *args, **kwargs):
		if request.POST['consulta']=="":
			return render(request,'finanzas/cobranza_list.html') 
		else:	
			try:				
				alumno = Alumno.objects.get(nombre__icontains=request.POST['consulta'])			
				cobranza = Cobranza.objects.filter(alumno=alumno,pagado=False)					 	
				c  = ConceptoCobro.objects.all() # esta es Fk de Cobranza 	
				today = date.today()
				try:
					beca = BecaAlumno.objects.get(alumno=alumno)
					for x in c: # Barre ConceptoCobro
						flp = x.fechaLimitePago					
						if today > flp:							
							for tt in cobranza: # Barre Cobranza
								if tt.concepto.id == x.id: 							   							
									tt.recargo = x.importeMulta											 
									tt.totalapagar = x.importe+Decimal(tt.recargo)
									tt.save()														 
						else:
							print beca.porcentaje						 				
							des = beca.porcentaje						
							td = x.importe*des/100
							tt = x.importe-td								
							for ttp in cobranza:
								if ttp.concepto.id == x.id: 				
									ttp.totalapagar = tt
									ttp.save()		
				except BecaAlumno.DoesNotExist:
					## aqui el alumno no tiene  beca
					beca = None 					
					for x in c: # Barre ConceptoCobro
						flp = x.fechaLimitePago					
						if today > flp:							
							for tt in cobranza: # Barre Cobranza
								if tt.concepto.id == x.id: 							   							
									tt.recargo = x.importeMulta											 
									tt.totalapagar = x.importe+Decimal(tt.recargo)
									tt.save()														 
						else:
							tt = x.importe
							for ttp in cobranza:
								if ttp.concepto.id == x.id: 				
									ttp.totalapagar = tt
									ttp.save()	
				return render(request,'finanzas/cobranza_list.html',{'alumno':alumno,'cobranza':cobranza }) 
			except Alumno.DoesNotExist:
				return render(request,'finanzas/cobranza_list.html') 


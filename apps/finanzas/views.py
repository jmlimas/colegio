from django.shortcuts import render
from django.http import  Http404,HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,TemplateView
from .models import ConceptoCobro, Banco,Cobranza,BecaAlumno
from .forms import AddConceptoForm,AddBancoForm,AddBecaAlumnoForm
from apps.principal.models import Alumno 
from django.core.urlresolvers import reverse
from datetime import date, datetime
from decimal import Decimal

from django.core import serializers
from django.core.mail import EmailMessage


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
							#print beca.porcentaje						 				
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

def ajax_RegistraPago(request):
	print 'mem'		 
	if request.is_ajax():	
		cob = Cobranza()
		cob = Cobranza.objects.get(id = request.GET['id_'])
		cob.tipopago ='Caja'
		cob.pagado = True
		cob.fechapago = datetime.now()
		cob.user = request.user
		cob.save()
		#send_email(request)
		cobranza = Cobranza.objects.filter(id=request.GET['id_'])
		cobranza_json = serializers.serialize('json',cobranza)
	    #print alumnos_json
		return HttpResponse(cobranza_json,content_type='application/json');
	else:
		print 'mem'	
		raise Http404
		

def send_email(request):
	cobro = Cobranza.objects.get(id=request.GET['id_'])	 
	email_padre = cobro.alumno.padre.email	
	nombre_padre = cobro.alumno.padre.nombre 
	#print email_padre
	#print cobro.concepto

	msg = EmailMessage(subject ='Gracias por su Pago',
						from_email = 'Jmlc  <agapo32@gmail.com',
						to = [email_padre])

	msg.template_name = 'graciasxpago'
	msg.template_content = {
		'std_content00' :'<H3><b>Gracias  por  realizar su pago :</h3></b><br><b>Del Mes:</b> %s <br><b>Sr.: </b> %s<br><b>Importe de su Pago:</b> %s'%(cobro.concepto, nombre_padre,cobro.totalapagar)
	}
	print msg
	msg.send()
# html_contenido = "<p>Sus credenciales de acceso al Sistema de Gestion Academica son: </p><br><br><b>Usuario: </b> %s <br><br><b>Password: </b> %s"%(usur2.username ,mi_clave)
#'std_content00' : '<h1> Gracias por su pago de %s, %s  </h1>' % (cobro.concepto, nombre_padre)		

def mostrar_alumnos22(request):	
	if request.is_ajax():
		alumnos = Alumno.objects.filter(grupo=request.GET['id_grupo'])	
		alumnos_json = serializers.serialize('json', alumnos)
		#print alumnos_json
		
		return HttpResponse(alumnos_json, content_type='application/json');
	else:
		raise Http404
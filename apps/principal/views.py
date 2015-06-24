from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render

from django.core.urlresolvers import reverse
from django.views.generic import View,ListView,CreateView,TemplateView,UpdateView,DetailView

from .models import Alumno,Materia,Empresa,MateriaxGrupo,Cicloescolar
from apps.finanzas.models import ConceptoCobro, Cobranza
from apps.configuracion.models import Grupo,Nivel,MaestroxGpo
from .forms import AddAlumnoForm, AddEmpresaForm, AddMateriaForm,AddMateriaxGrupoForm,AddCicloForm
 
from django.core import serializers

import json
from django.core.serializers.json import DjangoJSONEncoder
 
from braces.views import LoginRequiredMixin

 
class IndexView(TemplateView):
	template_name = 'principal/index.html'

class MyLogin(View):
	def post(self, request, *args, **kwargs):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)  
				#return HttpResponseRedirect("principal/index.html")
				return render(request,'principal/index.html')
			else:
				return render(request,'principal/noactivo.html')
		else:
			return render(request,'principal/nousuario.html')


class Cerrar(View):	
	def get(self, request, *args, **kwargs):
		logout(request)
		return HttpResponseRedirect('/')


class UsuarioDetailView(DetailView):
	model = User
	context_object_name = 'usuario'
	template_name = "principal/privado.html"


class AddEmpresa(CreateView):
	model = Empresa
	form_class = AddEmpresaForm
	success_url = '/listaemp'


class ListaEmpresa(ListView):
	context_object_name = 'empresas'
	model = Empresa

class AddCiclo(CreateView):
	form_class = AddCicloForm
	template_name = 'principal/ciclo_form.html'
	success_url = '/listciclo'

class ListCiclo(ListView):
	context_object_name = 'ciclo'
	model = Cicloescolar

class UpdateCiclo(UpdateView):
	form_class = AddCicloForm
	template_name = 'principal/ciclo_form.html' # yo lo bautice con ciclo_form.html   y deberia ser cicloescolar__form.html par que  fuera por default y no  ncesito esta  linea..
	model = Cicloescolar

	def get_success_url(self):
		return reverse('principal:list_cliclo')


class AddAlumnoCreateView(LoginRequiredMixin,CreateView):
	model = Alumno
	form_class = AddAlumnoForm	 
	success_url= '/listgpo/%s'	

	def get_success_url(self):	
		url = self.success_url % self.object.grupo.pk 
		return  url  # aqui le paso  el  /listgpo/5 al success_url 

	def post(self, request, *args, **kwargs):
		post = super(AddAlumnoCreateView,self).post(request, *args, **kwargs)
		self.GrupoSave(request.POST['grupo'])	# aqui le paso el  grupo al que le  va a sumar 1	 
		self.CobranzaSave(self.object.id)
		return post
		
	def GrupoSave(self,grupo):
		grupo = Grupo.objects.get(pk = grupo)
		grupo.numalumnos = grupo.numalumnos + 1
		grupo.save()

	def CobranzaSave(self,id):		
		#conceptos = ConceptoCobro.objects.all()	
		alumno = Alumno.objects.get(pk=id)	
		conceptos = ConceptoCobro.objects.filter(nivel = alumno.nivel)
		for item in conceptos:
			cobranza = Cobranza(alumno=alumno,concepto=item)
 			cobranza.save()
 	
class UpdateAlumno(LoginRequiredMixin,UpdateView):
	form_class = AddAlumnoForm
	model = Alumno 		

	def form_valid(self,form):			
		form.instance.user = self.request.user
		return super(UpdateAlumno, self).form_valid(form)

	def form_invalid(self,form):
		return super(UpdateAlumno, self).form_invalid(form)
	
	def get_success_url(self):	
		return reverse('principal:lista_alumnosall')
	 
	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(UpdateAlumno, self).get_context_data(**kwargs)
		#context['foto'] = kwargs={'pk': self.get_object().id}
		#context['foto'] = Alumno.objects.get(pk=self.kwargs['pk'])	
		context['foto'] = context['object'].foto # 3 maneras de hacer si  hay foto o alumno		 
		return context
 	

class InibuscalumnoView(TemplateView):
	template_name = 'principal/busca_alumno.html'
	

def consulta(request):
	if request.GET['consulta']=="":
		return render(request,'principal/busca_alumno.html')
	else:
		alumnos = Alumno.objects.filter(nombre__icontains=request.GET['consulta'])
		dic = {'alumnos':alumnos}
		return render(request,'principal/busca_alumno.html',dic) 


class ListAlumnos(ListView):
	context_object_name = 'alumnos'
	queryset = Alumno.objects.all().order_by('-created')[:4]



class AddMateriaCreateView(CreateView):
	form_class = AddMateriaForm
	model = Materia
	success_url = "/listmat"

	def post(self,request, *args, **kwargs):
		post = super(AddMateriaCreateView,self).post(request,*args, **kwargs)
		gpo = Grupo.objects.filter(grado = request.POST['grado'])	
		nveid = Nivel.objects.get(id = request.POST['nivel'])
		matid = Materia.objects.get(id = self.object.id)
		for e in gpo:
			matxasignar=MateriaxGrupo(nivel=nveid,materia=matid,grupo=e)
			matxasignar.save() 
 		return post
 

class ListMateriaView(ListView): # materias x Nivel ver 1.1
	context_object_name = 'niveles'
	model = Nivel
	template_name = "principal/listmateria.html"
 

def Lista_Materias(request): # ajax de materias por nivel ver 1.1
	if request.is_ajax():
		mats = Materia.objects.filter(nivel = request.GET['id_nivel'])		
		secciones=[]
		for indice,elemento in enumerate(mats):
			secciones.append({
				'pk':mats[indice].pk,
				'materia':mats[indice].materia,
				'grado':mats[indice].grado.nombre,
				'nivel':mats[indice].nivel.Nombre,
				})				
		data = json.dumps(secciones,cls=DjangoJSONEncoder)
		return HttpResponse(data, content_type="application/json")
	else:
		raise Http404
 
 
class UpdateMat(UpdateView):
	form_class = AddMateriaForm
	model = Materia
	def get_success_url(self):
		return reverse('principal:list_mat') 
		

class ListGpopk(CreateView):
	model = Grupo
	context_object_name = 'grupos'	
	template_name = "principal/demonivel.html"	

	
class ListAlumnoxgrupo(ListView): #List Alumnos x Grupo
	model = Nivel
	context_object_name = 'niveles'
	template_name = "principal/alumnosxgrupo.html"
	paginate_by = 2


def mostrar_grupos(request):	
	if request.is_ajax():		
		id_nivel = request.GET['id_nivel']
		grupos = Grupo.objects.filter(nivel=id_nivel)
	grupos_json = serializers.serialize('json', grupos)
	return HttpResponse(grupos_json, content_type='application/json'); 
	#else:
	#	raise Http404
	

def mostrar_alumnos22(request):	
	if request.is_ajax():
		alumnos = Alumno.objects.filter(grupo=request.GET['id_grupo'])	
		alumnos_json = serializers.serialize('json', alumnos)
		#print alumnos_json
		
		return HttpResponse(alumnos_json, content_type='application/json');
	else:
		raise Http404


def mostrar_alumnos(request):	   
	alumnos = Alumno.objects.filter(grupo = request.GET['id_grupo'])
	# con esto  obtengo (lpap) los padres de los alumnos del grupo
    # es la  unica manaera de  hacer  obtener  los  padres	 
	#lpap=[]
	#for alumno in alumnos:
	#	lpap = alumno.padre.id,alumno.padre.nombre,alumno.padre.ocupacio
	#print lpap
	secciones=[]
	for indice,elemento in enumerate(alumnos):		 
		#secciones.append({ 	
		#	'alumno':alumnos[indice].nombre+' '+alumnos[indice].apellidos,
		#	'grupo': alumnos[indice].grupo.nombre,
		#	'padre': alumnos[indice].padre.nombre,
		#	'email': alumnos[indice].padre.email,
		secciones.append({ 	
			'id':alumnos[indice].id,
			'alumno':alumnos[indice].nombre+' '+alumnos[indice].apellidos, 
			'grupo': alumnos[indice].grupo.nombre,
			})
	data = json.dumps(secciones,cls=DjangoJSONEncoder)
	return HttpResponse(data, content_type="application/json")


class ListMatxGpoNivel(ListView): # Materias por grupo 1.1 
	context_object_name = 'niveles'
	model = Nivel
	template_name = "principal/materiaxgrupo_list.html"


def listar_materiaxgpo(request): # Materias por grupo 1.1 
	mats = MaestroxGpo.objects.filter(grupo = request.GET['id_grupo'])
	secciones=[]
	for indice,elemento in enumerate(mats):		 
		secciones.append({ 
		    'id': mats[indice].id,	
			'materia': mats[indice].materia.materia,
			'grupo': mats[indice].grupo.nombre,
			'nivel': mats[indice].nivel.Nombre,	
			'maestro': mats[indice].maestro.nombre,							
			}) 		 
	data = json.dumps(secciones,cls=DjangoJSONEncoder)	
	return HttpResponse(data, content_type="application/json")


#materias asiganadas por grupo
class addMatxGpo(CreateView):
	model = MateriaxGrupo
	form_class = AddMateriaxGrupoForm
	success_url = '/list_matasiganada'


class ListMatAsignada(ListView): #materias asiganadas por grupo
	model = MateriaxGrupo
	context_object_name = 'asignadas'
	template_name = "principal/materiasignada_list.html"


class UpdateMatxGpo(UpdateView):
	form_class= AddMateriaxGrupoForm
	model = MateriaxGrupo
	def get_success_url(self):
		return reverse('principal:list_matasiganada')
 

def mostrarmatxgpo(request):
	if request.is_ajax():			 
		matxgpos = MateriaxGrupo.objects.filter(grupo = request.GET['id_grupo'],status = True)
		secciones=[]
		for indice,elemento in enumerate(matxgpos):
			secciones.append({
				'id':matxgpos[indice].materia.id,
				'materia':matxgpos[indice].materia.materia,				
				})
		data = json.dumps(secciones,cls=DjangoJSONEncoder)
		print data
		return HttpResponse(data, content_type='application/json');
	else:
		raise Http404
 
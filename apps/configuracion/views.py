from django.http import HttpResponse,Http404
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, TemplateView,UpdateView
from .models import Nivel,Grado,Grupo,Maestro,Padre,Seccion,MaestroxGpo
from .forms import AddNivelForm,AddGrupoForm,AddMaestroForm,AddPadreForm
from .forms import AddSeccionForm,AddGradoForm,MaestroxGpoForm
from apps.principal.models import Alumno
from braces.views import LoginRequiredMixin,GroupRequiredMixin
from django.core import serializers 
from django.shortcuts import render

import json
from django.core.serializers.json import DjangoJSONEncoder


class AddGradoCreateView(CreateView):
	form_class = AddGradoForm
	model = Grado
	success_url = '/listgrado'
	  

class ListGrados(ListView):
	context_object_name = 'grados'
	model = Grado
	paginate_by = 6

class UpdateGrado(UpdateView):
	model = Grado

	def get_success_url(self):
		return reverse('configuracion:list_grados')


class AddNivelCreateView(LoginRequiredMixin,GroupRequiredMixin,CreateView):
	model = Nivel
	form_class = AddNivelForm 
	success_url = '/listnivel'
	group_required = "cordinacion"

class ListaNivel(LoginRequiredMixin,GroupRequiredMixin,ListView):
	context_object_name = 'niveles'
	model = Nivel
	group_required = "cordinacion"
	

class NivelUpdate(LoginRequiredMixin,GroupRequiredMixin,UpdateView):
	model = Nivel
	group_required = "codinacion"

	def get_success_url(self):
		return reverse('configuracion:list_nivel')		
 

class AddGrupoCreateView(LoginRequiredMixin,GroupRequiredMixin,CreateView):
	form_class = AddGrupoForm
	model = Grupo
	success_url = '/listgpos/'
	group_required = "cordinacion"
	
	#def GrupoSave(self,request, *args, **kwargs):
	#	context = super(ListGpoDetailView,self).get_context_data(**kwargs)
	#	grupo = Grupo()
	#	grupo = Grupo.objects.get(pk = context['pk'])
	#	grupo.numalumnos = grupo.numalumnos + 1
	#	grupo.save()

 
class ListGpos(ListView):	
	context_object_name = 'niveles'	
	model = Nivel
	template_name = 'configuracion/grupo_list.html'
	paginate_by = 6


def Lista_GruposAjax(request): # ajax de materias por nivel ver 1.1
	mats = Grupo.objects.filter(nivel = request.GET['id_nivel'])
	secciones=[]
	for indice,elemento in enumerate(mats):
		secciones.append({
			'pk':mats[indice].pk,
			'nombre':mats[indice].nombre,
			'nivel':mats[indice].nivel.Nombre,
			'grado':mats[indice].grado.nombre,
			'seccion':mats[indice].seccion.nombre,
			'maximo':mats[indice].maximo,
			'numalumnos':mats[indice].numalumnos,
			'cupo':mats[indice].cupo(),
			})				
	data = json.dumps(secciones,cls=DjangoJSONEncoder)
	return HttpResponse(data, mimetype="application/json")
  

def Lista_GruposAjax2(request):	
	mats = Grupo.objects.filter(nivel = request.GET['id_nivel'])
	mats_json = serializers.serialize('json',mats)
	#mats_json = serializers.serialize('json', [x.mats for x in mats])
	return 	HttpResponse(mats_json,content_type='application/json')



class AlumnosGpoListView(ListView):
	model = Alumno
	context_object_name = 'alumnos'

	def get_context_data(self, **kwargs):
		context = super(AlumnosGpoListView,self).get_context_data(**kwargs)
		# print self.kwargs['id']  Este es  el  parametro que  biene de la  url
		context['alumnos'] = Alumno.objects.filter(grupo=self.kwargs['id']) #  Este es  el  parametro que  biene de la  url
		return context


def AlumnosGpo(request,id): # esta  funcion y  la  class AlumnosGpoListView son lo mismos con su metodo correspondiente lo dejo como ejeplo
	alum = Alumno.objects.filter(grupo=id)
	ctx = {'alumnos':alum}
	return render(request,'principal/alumno_list.html',ctx)	


class ListGpoDetailView(TemplateView):
	model = Alumno
	template_name = 'principal/alumno_detail.html'

	def get_context_data(self, **kwargs):
		context = super(ListGpoDetailView,self).get_context_data(**kwargs)
		context ['gpo'] = self.model.objects.filter(grupo = context['pk'])
		context ['gp'] = Grupo.objects.filter(id= context['pk']) # es  para pintar alumnos  minimos  y maximos
		# pero  filta  solo del grupo  dende se esta  trabajando
		#print context
		return context


class UpdateGrupo(LoginRequiredMixin, UpdateView):
	form_class = AddGrupoForm
	model = Grupo
	#queryset = None

	#def get_context_data(self, **kwargs):		 
	#	context = super(UpdateGrupo,self).get_context_data(**kwargs)
	#	context['numa'] = context['object'].numalumnos	# numa es una  variable		 
	#	return context # la variable  numa la  despliego en el  formulario {{numa}}

	#def form_valid(self,form):	
	#	form.instance.user = self.request.user
	#	return super(UpdateView, self).form_valid(form)

	#def form_invalid(self,form):		 
	#	return super(UpdateView, self).form_invalid(form)

	def get_success_url(self):
		return reverse('configuracion:list_gpo')


class AddProfeCreateView(CreateView):
	model = Maestro
	form_class = AddMaestroForm
	success_url = '/listprofe'


class ListProfe(ListView):
	context_object_name = 'maestros'
	model = Maestro
	paginate_by = 5

	def get_context_data(self, **kwargs):
		context = super(ListProfe,self).get_context_data(**kwargs)		
		niveles = [maestro.nivel.all() for maestro in context['maestros']]
		context['maestro_nivel']= zip(context['maestros'],niveles)
		return context 
		
		# niveles = carga todos los niveles y los recorre de la tabla maestros
		# y con zip junta maestros y niveles para mostras los niveles
		# donde trabajan los profes

class UpdateProfe(UpdateView):
	model = Maestro
	form_class = AddMaestroForm

	def get_success_url(self):
		return reverse('configuracion:list_profe')


class AddMstroxGpo(LoginRequiredMixin,CreateView):
	model = MaestroxGpo
	form_class = MaestroxGpoForm
	success_url = '/listmatxgpos'

class UpMaestroxGpo(UpdateView):
	model = MaestroxGpo
	form_class = MaestroxGpoForm

	def get_success_url(self):
		return reverse('principal:lista_matxgpo')




def mostrarnivel(request):
	if request.is_ajax():		
		lisnivel = Nivel.objects.filter(maestro=request.GET['id_maestro']) # funciona por que Nivel y maestro estan relacionados me trae el nivel del maestro en truno
		lisnivel_json = serializers.serialize('json',lisnivel)
		return HttpResponse(lisnivel_json,content_type='application/json');
	else:
		raise Http404
 

class AddPadre(CreateView):
	form_class = AddPadreForm
	template_name = 'configuracion/padre_form.html'
	#success_url = reverse_lazy('list_padre')
	success_url = '/listpadre/'



class ListPadre(ListView):
	context_object_name = 'padres'
	model = Padre
	paginate_by =8


class UpdatePadre(UpdateView):
	model = Padre

	def get_success_url(self):
		return reverse('configuracion:list_padre')


class AddSeccion(CreateView):
	model = Seccion
	form_class = AddSeccionForm
	success_url = '/listsecc/'
	

class ListSecc(ListView):
	context_object_name = 'secciones'
	model = Seccion


class UpdateSecc(UpdateView):
	form_class = AddSeccionForm
	model = Seccion

	def get_success_url(self):
		return reverse('configuracion:list_seccion') 

class MaestroxGrupoDetailView(ListView):
	model = MaestroxGpo
	template_name = 'configuracion/maestroxgpo_list.html'
	def get_context_data(self, **kwargs):
		context = super(MaestroxGrupoDetailView,self).get_context_data(**kwargs)
		context['profe'] = MaestroxGpo.objects.filter(maestro=self.kwargs['pk'])
		print context
		return context

 

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import CreateView,ListView
from apps.principal.forms import AddCalForm
from .models import Asistencia
from apps.principal.models import Alumno,Calificacion,Mes, Materia
from apps.configuracion.models import Nivel

from django.core import serializers
from datetime import datetime

# Create your views here.

class AddAsistenciasView(ListView):
	context_object_name = 'alumnos'
	model = Alumno 
   	template_name  = 'maestro/asistencia3_form.html'
	success_url = '/listasistencia'      	

def asistencias(request):        
    niveles = Nivel.objects.all()
    alumnos = Alumno.objects.filter(grupo=2)
    ctx = {'alumnos': alumnos,'niveles':niveles} 
    return render(request,'maestro/asistencia3_form.html',ctx)


def asistencias2(request):
    estudiantes = Asistencia.objects.all()
    if request.method == 'POST':
        for i in range(estudiantes.count()):
            asistencia = request.POST['asistencia%s' % i] 
            print  asistencia          
    context = {'estudiantes': estudiantes}
    return render(request, 'asistencia_form.html', context)
    

def ajax_asistencia(request): 
    alumno = request.GET['id_alumno']     
    if request.GET['id_op'] != 'A':
        asi = Asistencia()   
        asi.alumno = Alumno.objects.get(id=alumno)
        asi.falta = request.GET['id_op']     
        asi.fecha = datetime.today()
        asi.save()  
        asis = Asistencia.objects.all()
        asis_json = serializers.serialize('json', asis) 
        return HttpResponse(asis_json,content_type='application/json');

def ajax_cargagrupo(request):
    if request.is_ajax():
        alumnos = Alumno.objects.filter(grupo=request.GET['id_grupo'])
        alumnos_json = serializers.serialize('json',alumnos)
        #print alumnos_json
        return HttpResponse(alumnos_json,content_type='application/json');
    else:
        raise Http404

 
class ListaAsistencia(ListView):
	context_object_name = 'asistencia'
	model = Asistencia

        def get_queryset(self):
            today = datetime.now()
            month = today.month
            print month
            return super(ListaAsistencia,self).get_queryset().filter(fecha__month=month)
 
 
 

class ListaCalificaciones(ListView):
    model = Nivel
    context_object_name = 'niveles'  
    template_name = "maestro/ListaCalifica.html"
    #template_name = "principal/materiaxgrupo_list.html"
 

class ListaCalificaciones1(ListView):
    context_object_name = 'calificaciones' 
    model = Calificacion

    def get_context_data(self, **kwargs):
        context = super(ListaCalificaciones1, self).get_context_data(**kwargs)
        context['meses'] = Mes.objects.all()
        context['materias'] = Materia.objects.all()
        context['alumnos'] = Alumno.objects.filter(grupo=1)
        return context


class AddCalCreateView(CreateView):
    model = Calificacion
    form_class = AddCalForm  
    success_url = "/listacal"
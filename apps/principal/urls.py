from django.conf.urls import patterns, url 
from .views import Cerrar,UsuarioDetailView,MyLogin,AddEmpresa,ListaEmpresa
from .views import AddCiclo,ListCiclo,UpdateCiclo,AddAlumnoCreateView
from .views import ListAlumnos,UpdateAlumno,consulta,InibuscalumnoView,AddMateriaCreateView,IndexView 
from .views import ListMateriaView,UpdateMat,ListGpopk,ListMatxGpoNivel,addMatxGpo,ListAlumnoxgrupo,ListMatAsignada,UpdateMatxGpo
from django.contrib.auth.decorators import login_required
 

urlpatterns = patterns('apps.principal.views',
#urlpatterns = patterns('',
	url(r'^$',IndexView.as_view(),name = 'index'),	  
	url(r'^my_login/$',MyLogin.as_view(),name='my_login'),
	url(r'^cerrar/$',login_required(Cerrar.as_view()),name='cerrar'),
	url(r'^user/(?P<pk>\d+)/$', UsuarioDetailView.as_view(), name='detalle_usuario'),
	url(r'^emp/$',AddEmpresa.as_view(),name = 'empresa'),
	url(r'^listaemp/$',ListaEmpresa.as_view(),name='lista_empresa'),
	url(r'^addciclo/$',AddCiclo.as_view(),name = 'add_ciclo'),
	url(r'^listciclo/$',ListCiclo.as_view(),name='list_cliclo'),
	url(r'^updateciclo/(?P<pk>\d+)/$',UpdateCiclo.as_view(),name='ciclo_update'),	
	url(r'^addalumno/$',AddAlumnoCreateView.as_view(),name='add_alumno'),
	url(r'^listalumnos/$',ListAlumnos.as_view(),name = 'lista_alumnosall'),
	url(r'^updatealumno/(?P<pk>\d+)/$',UpdateAlumno.as_view(),name='alumno_update'),
	url(r'^consulta/$',consulta),
	url(r'^inibuscal/$',InibuscalumnoView.as_view()),	
	url(r'^addmat/$', AddMateriaCreateView.as_view(),name = 'add_mat'),
	url(r'^listmat/$',ListMateriaView.as_view(),name = 'list_mat'),
	url(r'^updatemat/(?P<pk>\d+)/$', UpdateMat.as_view(), name='materia_update'),
	url(r'^listgrupopk/$',ListGpopk.as_view(),name='list_grupopk'),
	url(r'^ajax/mostrar-grupos/$', "mostrar_grupos"),
	url(r'^ajax/listgpo/$',"mostrar_alumnos"),
	#url(r'^listmatxgpos/$',ListaNivel.as_view(),name='lista_matxgpo'),
	url(r'^listmatxgpos/$',ListMatxGpoNivel.as_view(),name='lista_matxgpo'),
	url(r'^listmatasignadas/$',ListMatAsignada.as_view(),name='list_matasiganada'),
	url(r'^upmatasigandas/(?P<pk>\d+)/$',UpdateMatxGpo.as_view(),name='matxasignar_uodate'),
	url(r'^materiasxgrupo/$',addMatxGpo.as_view(),name='materias_x_grupo'),
	url(r'^ajax/listar_materiaxgpo/$',"listar_materiaxgpo"),
	url(r'^ajax/materias-grupos/$',"mostrarmatxgpo"),
	url(r'^ajax/listamat/$',"Lista_Materias"),
	url(r'^listalumxgpo/$',ListAlumnoxgrupo.as_view()),
)

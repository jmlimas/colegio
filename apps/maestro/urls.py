from django.conf.urls import patterns, url
from .views import AddAsistenciasView,ListaAsistencia,ListaCalificaciones,AddCalCreateView

urlpatterns = patterns('apps.maestro.views',
	url(r'^addasistenciax/$', AddAsistenciasView.as_view(),name = 'add_asistencias'),  
	url(r'^listasistencia/$',ListaAsistencia.as_view(),name = 'list_asistencias'), 
	url(r'^addasistencia/$','asistencias'),
	url(r'^ajax/asis/$',"ajax_asistencia"),
	url(r'^ajax/asisxgrupo/$',"ajax_cargagrupo"),
	url(r'^listacal/$',ListaCalificaciones.as_view(),name='lista_calificaciones'),
	url(r'^addcal/$', AddCalCreateView.as_view(),name='add_cal'),
)   
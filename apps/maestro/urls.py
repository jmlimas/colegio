from django.conf.urls import patterns, url
from .views import AddAsistenciasView,ListaAsistencia,ListaCalificaciones,AddCalCreateView

urlpatterns = patterns('', 
	url(r'^addasistenciaz/$', AddAsistenciasView.as_view(),name = 'add_asistencias'),  
	url(r'^listasistencia/$',ListaAsistencia.as_view(),name = 'list_asistencias'), 
	url(r'^addasistencia/$','apps.maestro.views.asistencias'),
	url(r'^ajax/asis/$',"apps.maestro.views.ajax_asistencia"),
	url(r'^ajax/asisxgrupo/$',"apps.maestro.views.ajax_cargagrupo"),
	url(r'^listacal/$',ListaCalificaciones.as_view(),name='lista_calificaciones'),
	url(r'^addcal/$', AddCalCreateView.as_view(),name='add_cal'),
)   
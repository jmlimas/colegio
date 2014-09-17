from django.conf.urls import patterns, url
from .views import AddTransporteView,ListTransporteView,ListAlumTrasp
from .views import AddAlumTransView,AddConducta,ListConducta

urlpatterns = patterns('',
	url(r'^addtransporte/$', AddTransporteView.as_view(),name = 'add_transporte'),  
	url(r'^listransporte/$',ListTransporteView.as_view(),name = 'list_transporte'),
	url(r'^listalumtrans/$',ListAlumTrasp.as_view(),name = 'list_alumnotrasporte'),
	url(r'^addalumtrans/$',AddAlumTransView.as_view(),name = 'add_alumnostransporte'),
	url(r'^addconducta/$',AddConducta.as_view(),name = 'add_conducta'),
	url(r'^listconducta/$',ListConducta.as_view(),name='list_conducta'),
)  
from django.conf.urls import patterns, url
from .views import AddConcepto,ListConceptos,UpdateConceptos,AddBancos
from .views import ListBancos,UpdateBancos,AddBecaAlumno,ListBecaAlumno
from .views import UpdateBeca,ListCobranza,ListPagoAtrasado

urlpatterns = patterns('apps.finanzas.views',
	url(r'^addconcepto/$', AddConcepto.as_view(),name = 'add_concepto'),  
	url(r'^listconceptos/$',ListConceptos.as_view(),name = 'list_conceptos'),
	url(r'^updateconceptos/(?P<pk>\d+)/$',UpdateConceptos.as_view(),name='conceptos_update'),   
    url(r'^addbancos/$',AddBancos.as_view(),name='add_bancos'),
    url(r'^listbancos/$',ListBancos.as_view(),name='list_bancos'),
    url(r'^updatebancos/(?P<pk>\d+)/$',UpdateBancos.as_view(),name='bancos_update'),
    url(r'^addbecaalumno/$',AddBecaAlumno.as_view(),name='add_becaalumnos'),
    url(r'^listbecaalumnos/$',ListBecaAlumno.as_view(),name = 'list_becaalumno'),
    url(r'^updatebecaalumnos/(?P<pk>\d+)/$',UpdateBeca.as_view(),name = 'beca_update'),
    url(r'^listcobros/$',ListCobranza.as_view(),name = 'list_cobros'), 
    url(r'^ajax/reg_pago/$',"ajax_RegistraPago"),
    url(r'^pagoatrasado/$',ListPagoAtrasado.as_view(),name='list_pagoatrasado'),
                             
)
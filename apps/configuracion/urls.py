from django.conf.urls import patterns, url
from .views import AddNivelCreateView,ListaNivel,NivelUpdate,AddGradoCreateView
from .views import ListGrados,UpdateGrado,AddGrupoCreateView,ListGpos,ListGpoDetailView
from .views import UpdateGrupo,AddProfeCreateView,ListProfe,UpdateProfe,AddPadre
from .views import AddMstroxGpo,ListPadre,UpdatePadre,AddSeccion,UpMaestroxGpo
from .views import ListSecc,UpdateSecc,AlumnosGpoListView,MaestroxGrupoDetailView



urlpatterns = patterns('',
	url(r'^addnivel/$', AddNivelCreateView.as_view(),name = 'add_nivel'),  
	url(r'^listnivel/$',ListaNivel.as_view(),name = 'list_nivel'),
    url(r'^updatenivel/(?P<pk>\d+)/$', NivelUpdate.as_view(), name='nivel_update'),
	url(r'^addgrado/$', AddGradoCreateView.as_view(),name = 'add_grado'),
    url(r'^listgrado/$',ListGrados.as_view(),name='list_grados'),
    url(r'^updategrado/(?P<pk>\d+)/$', UpdateGrado.as_view(), name='grado_update'),
    url(r'^addgrupo/$',AddGrupoCreateView.as_view(),name= 'add_grupo'),
    url(r'^listgpos/$',ListGpos.as_view(),name = 'list_gpo'),
    url(r'^listgpo/(?P<pk>\d+)/$',ListGpoDetailView.as_view(),name='list_gpodet'),
    url(r'^updategrupo/(?P<pk>\d+)/$',UpdateGrupo.as_view(),name='grupo_update'),
    url(r'^addprofe/$',AddProfeCreateView.as_view(),name = 'add_profe'),
    url(r'^listprofe/$',ListProfe.as_view(),name = 'list_profe'),
    url(r'^updateprofe/(?P<pk>\d+)/$',UpdateProfe.as_view(),name='update_profe'),
    url(r'^addpadre/$',AddPadre.as_view(),name = 'add_padre'),
    url(r'^addmstroxgpo/$',AddMstroxGpo.as_view(),name='add_maestrpxgpo'),
    url(r'^upmstroxgpo/(?P<pk>\d+)/$',UpMaestroxGpo.as_view(),name='up_maestrxgpo'),
   # url(r'^listmstroxgpo/$',Listmstroxgpo.as_view(),name = 'list_mastroxgpo'),
    url(r'^ajax/mostrar-nivel/$', "mostrarnivel"),
    url(r'^listpadre/$',ListPadre.as_view(),name='list_padre'),
    url(r'^updatepadre/(?P<pk>\d+)/$',UpdatePadre.as_view(),name='update_padre'),
    url(r'^addsecc/$',AddSeccion.as_view(),name = 'add_seccion'),
    url(r'^listsecc/$',ListSecc.as_view(),name='list_seccion'),
    url(r'^updatesecc/(?P<pk>\d+)/$', UpdateSecc.as_view(), name='nivel_update'),
    url(r'^alumnosgrupo/(?P<id>\d+)/$', AlumnosGpoListView.as_view(), name='alumnosgpo_listview'),
    url(r'^ajax/listagpo/$',"Lista_GruposAjax"),
    url(r'^detmaestroxgpo/(?P<pk>\d+)/$', MaestroxGrupoDetailView.as_view(),name='det_maestroxgpo'),
    #url(r'^alumnosgrupo/(?P<id>\d+)/$',"AlumnosGpo", name='alumnosgpo_listview'), la url de arriba es la  mismo que esta  esta es para un funcion de ejemplo 
)   
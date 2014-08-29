from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover() 
from apps.principal.views import IndexView 


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sigamosaprendiendo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),   
    url(r'^', include('apps.principal.urls',namespace ='principal')),
    url(r'^', include('apps.configuracion.urls', namespace='configuracion')),    
    url(r'^', include('apps.finanzas.urls', namespace='finanzas')),    
    url(r'^', include('apps.maestro.urls',namespace='maestro')),
    url(r'^', include('apps.trasporte.urls',namespace='trasporte')),
	url(r'^$',IndexView.as_view(),name = 'index'),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
	
 )

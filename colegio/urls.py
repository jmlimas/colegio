from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
 
admin.autodiscover()  


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),  
    
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT, } ),

    url(r'^', include('apps.principal.urls',namespace ='principal')),
    url(r'^', include('apps.configuracion.urls', namespace='configuracion')),    
    url(r'^', include('apps.finanzas.urls', namespace='finanzas')),    
    url(r'^', include('apps.maestro.urls',namespace='maestro')),
    url(r'^', include('apps.trasporte.urls',namespace='trasporte')),
	 
 )

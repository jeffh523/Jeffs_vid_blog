from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	
	url(r'^$', 'Blog.views.home', name='home'),
	
	url(r'^asteroid_field', 'Blog.views.asteroid_field', name='asteroid_field'),

	url(r'^admin/', include(admin.site.urls)),
	
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.STATIC_ROOT}),
		
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
		{'document_root': settings.MEDIA_ROOT}),
)  
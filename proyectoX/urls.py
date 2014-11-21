from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  
  	url(r'^$', 'principal.views.inicio', name="inicio"),

    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drisapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'drisapp.core.views.index', name='index'),
    url(r'^about/$', 'drisapp.core.views.about', name='about'),
    url(r'^contact/$', 'drisapp.core.views.contact', name='contact'),
    url(r'^calculate/$', 'drisapp.core.views.calculate', name='calculate'),
    url(r'^relatorio/$', 'drisapp.core.views.relatorio', name='relatorio'),
    url(r'^admin/', include(admin.site.urls)),
)

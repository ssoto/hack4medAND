from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lisa_graph.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'lisa_search.views.index', name='index'),
    url(r'^search$', 'lisa_search.views.search', name='search'),
    url(r'^upload$', 'lisa_search.views.upload', name='upload'),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
)

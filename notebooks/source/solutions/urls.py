from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wikicamp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^wikicamp/(?P<page_name>[^/]+)/edit/$','wiki.views.edit_page'),
    (r'^wikicamp/(?P<page_name>[^/]+)/save/$','wiki.views.save_page'),
    (r'^wikicamp/(?P<page_name>[^/]+)/$','wiki.views.view_page'),
    #(r'^admin/(.*)', admin.site.root),
    (r'^wikicamp/$', 'wiki.views.index'),

)

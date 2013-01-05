from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('photo_app.views',
    # Examples:
    # url(r'^$', 'photo_sharing.views.home', name='home'),
    # url(r'^photo_sharing/', include('photo_sharing.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'index', name="index"),
    url(r'^photo/(?P<photo_id>\d+)/$', 'view_photo', name="view_photo"),
    url(r'^photo/(?P<photo_id>\d+)/comment/$', 'comment', name="comment"),
    #url(r'^save_photo/$', 'save_photo'),

)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
    urlpatterns += patterns('',
               (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
              )
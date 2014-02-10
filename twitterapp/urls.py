from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

# Views
from views import Index

urlpatterns = patterns('',
    # Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Third Party Url
    url(r'', include('social_auth.urls')),

    # Pages Views
    url(r'^$', Index.as_view(), name='index'),

    # App url redirects
    url(r'^account/$', include('accounts.urls', namespace='accounts')),
    url(r'^tweet/$', include('tweets.urls', namespace='tweets'))

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )


from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('events.views',
    url(r'^$', 'index'),
    url(r'^events/(?P<namespace>[-a-z0-9]+)/$', 'detail'),
    
)


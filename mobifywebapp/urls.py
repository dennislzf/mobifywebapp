from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#URL patterns for mobify web application
urlpatterns = patterns('',url(r'^$','mobifywebapp.views.index'),
   url(r'^get-counter', 'mobifywebapp.views.getcounter'),
    url(r'^cached-timestamp', 'mobifywebapp.views.cachedtimestamp'),
    url(r'^increment-counter', 'mobifywebapp.views.incrementcounter'),
    url(r'^echo', 'mobifywebapp.views.echo'),
    url(r'^get-sized-image/(?P<width>\d+)/(?P<height>\d+)/$','mobifywebapp.views.getsizedimage'),
     (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
      {'document_root': settings.MEDIA_ROOT}),
   

)

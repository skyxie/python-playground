from django.conf.urls import patterns, include, url
import services.views

urlpatterns = patterns('',
    url(r'authorize/(?P<service_id>[0-9]*)$', services.views.authorize, name='authorize'),
    url(r'foursquare_callback$', services.views.foursquare_callback, name='foursquare_callback')
)

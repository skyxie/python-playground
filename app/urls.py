from django.conf.urls import patterns, include, url
import app.views

urlpatterns = patterns('',
    url(r'^services', include('services.urls')),
    url(r'^$', app.views.home, name="home")
)

from django.http import HttpResponse, HttpResponseRedirect
from services.models import Oauth2, Service
import logging

logger = logging.getLogger('django.request')

def authorize(request, service_id):
  s = Oauth2.objects.get(service_id=service_id)
  return HttpResponseRedirect(s.full_login_url())

def foursquare_callback(request):
  code = request.GET.get("code")
  logger.debug("code:" + code)
  return HttpResponse(code)

def facebook_callback(request):
  code = request.GET.get("code")
  logger.debug("code:" + code)
  return HttpResponse(code)

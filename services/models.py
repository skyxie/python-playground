from django.db import models
import logging

class Service(models.Model):
  name = models.CharField(max_length = 200)
  url = models.CharField(max_length = 200)
  client_id = models.CharField(max_length = 200)
  client_secret = models.CharField(max_length = 200)

  def __unicode__(self):
    return self.name

class Oauth2(models.Model):
  service = models.ForeignKey(Service)
  login_url = models.CharField(max_length = 200)
  access_token_url = models.CharField(max_length = 200)
  callback_url = models.CharField(max_length = 200)

  def __unicode__(self):
    return self.service.name

  def full_login_url(self):
    query_params = {
      'client_id' : self.service.client_id,
      'response_type' : 'code',
      'redirect_uri' : self.callback_url
    }
    query_params_array = []
    for key, val in query_params.items():
      query_params_array.append("%s=%s" % (key, val))
    full_login_url = self.login_url + "?" + "&".join(query_params_array)
    return full_login_url


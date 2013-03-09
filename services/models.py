from django.db import models

class Service(models.Model):
  name = models.CharField(max_length = 200)
  url = models.CharField(max_length = 200)
  client_id = models.CharField(max_length = 200)
  client_secret = models.CharField(max_length = 200)

class Oauth2(models.Model):
  service = models.ForeignKey(Service)
  login_url = models.CharField(max_length = 200)
  access_token_url = models.CharField(max_length = 200)
  callback_url = models.CharField(max_length = 200)

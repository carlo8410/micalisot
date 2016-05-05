from django.db import models

# Create your models here.
class Usuario(models.Model):
      u_nombre = models.CharField(max_length = 200)


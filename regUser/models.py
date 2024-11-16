from django.db import models

# Create your models here.
class regUser(models.Model):
	usuario = models.CharField(max_length=32)
	apellido = models.CharField(max_length=32)
	nombre = models.CharField(max_length=32)

	def __str__(self):
		return self.usuario

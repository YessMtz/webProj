from django.db import models

# Create your models here.
#class loginDB(models.Model):
#	content = models.CharField(max_length=256)
#	timestamp = models.DateTimeField(auto_add_now=True)

class inicio(models.Model):
	content = models.CharField(max_length=256)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content
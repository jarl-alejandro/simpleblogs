from django.db import models

class Entrada(models.Model):
	titulo = models.CharField(max_length = 140)

	def __unicode__(self):
		return self.titulo
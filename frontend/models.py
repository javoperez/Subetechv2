from django.db import models
from django.utils.encoding import smart_unicode ##Para evitar errores en el return

# Create your models here.
class Comentario(models.Model):
	nombre= models.CharField(max_length=40,null=True, blank=True)
	email= models.EmailField(null=False, blank=False)
	timestamp= models.DateTimeField(auto_now_add=True, auto_now= False)
	comentario= models.TextField(max_length=500,null=True, blank=True)

	def __unicode__(self):
		return smart_unicode(self.nombre)

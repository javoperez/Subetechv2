from django.db import models

# Create your models here.


class Alumno(models.Model):
	def __unicode__(self):  
		return self.matricula
	nombre1 = models.CharField(max_length=20)
	nombre2= models.CharField(max_length=20, null=True, blank=True) # Ojo, puede ser nulo
	ap_paterno= models.CharField(max_length=20)
	ap_materno= models.CharField(max_length=20)
	matricula= models.CharField(max_length=10)
	fecha_alta = models.DateField('Inicio')
	contrasena= models.CharField(max_length=30)
	encriptado= models.CharField(max_length=100, null=True, blank= True) 

class Ruta(models.Model):
	def __unicode__(self):  
		return self.nombre
	nombre=models.CharField(max_length=40)
	salida=models.TimeField("Hora Salida")
	llegada= models.TimeField("Hora Llegada")
	kilometraje= models.IntegerField(max_length=5)

class RegistroSalida(models.Model):
	def __unicode__(self):  
		return unicode(self.fechaOut)
	identificador = models.ForeignKey('Alumno')
	fechaOut= models.DateField("Fecha")
	horaOut= models.TimeField("Hora")
	latitud= models.FloatField(default=0)
	longitud= models.FloatField(default=0)

class RegistroEntrada(models.Model):
	def __unicode__(self):  
		return unicode(self.fechaIn) # Necesito pasar el unicode de fecha
	#Folio= ID
	identificador = models.ForeignKey('Alumno')
	fechaIn= models.DateField("Fecha")
	horaOut= models.TimeField("Hora")
	latitud= models.FloatField(default=0)
	longitud= models.FloatField(default=0)

class Camion(models.Model):
	def __unicode__(self):  
		return self.nombre
	#id= por default
	nombre= models.CharField(max_length=40)
	latitud= models.FloatField(default=0)
	longitud= models.FloatField(default=0)
	velocidad= models.FloatField(default=0)
	placa= models.CharField(max_length= 20)
	asientos= models.IntegerField(max_length=60)

class Cobro(models.Model):

	cantidad=models.IntegerField(max_length=7)

class Cuenta(models.Model):
	#numeroCuenta=ID
	identificador = models.ForeignKey('Alumno', null=True, blank= True)
	tipoServicio=models.CharField(max_length=20)
	saldo= models.IntegerField(max_length=4)

class Deposito(models.Model):
	#ID= Folio
	cantidad= models.IntegerField(max_length=4)
	fechaDeposito= models.DateTimeField("Fecha Deposito")




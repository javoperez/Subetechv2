from django.contrib import admin
from backend.models import Alumno, Ruta, RegistroEntrada,RegistroSalida, Camion
from backend.models import Cobro, Cuenta, Deposito
import datetime
# Register your models here.

class AlumnoAdmin(admin.ModelAdmin):
	list_display = ('nombre1', 'nombre2', 'ap_paterno', 'ap_materno', 'matricula','encriptado')
	list_filter=['matricula']

class RutaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'kilometraje','salida','llegada')

class RegEntradaAdmin(admin.ModelAdmin):
	list_display= ('id', 'identificador', 'fechaIn','latitud', 'longitud')
	list_filter=['fechaIn']

class RegSalidaAdmin(admin.ModelAdmin):
	list_display= ('id', 'identificador', 'fechaOut','latitud', 'longitud')
	list_filter=['fechaOut']

class CamionAdmin(admin.ModelAdmin):
	list_display=('nombre','placa', 'asientos', 'velocidad','latitud','longitud')
	list_filter=['nombre']

class CobroAdmin(admin.ModelAdmin):
	list_display= ('id','cantidad')
	
class CuentaAdmin(admin.ModelAdmin):
	list_display= ('id', 'identificador', 'tipoServicio','saldo')

class DepositoAdmin(admin.ModelAdmin):
	list_display= ('id','cantidad','fechaDeposito')

admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Ruta,RutaAdmin)
admin.site.register(RegistroSalida,RegSalidaAdmin)
admin.site.register(RegistroEntrada,RegEntradaAdmin)
admin.site.register(Camion,CamionAdmin)
admin.site.register(Cobro,CobroAdmin)
admin.site.register(Cuenta,CuentaAdmin)
admin.site.register(Deposito,DepositoAdmin)


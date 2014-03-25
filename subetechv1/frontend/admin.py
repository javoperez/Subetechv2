from django.contrib import admin
from frontend.models import Comentario
import datetime
# Register your models here.

class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'email', 'timestamp', 'comentario')

admin.site.register(Comentario,ComentarioAdmin)
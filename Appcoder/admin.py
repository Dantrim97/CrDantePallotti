from django.contrib import admin
from .models import Cliente,Equipos,Servicios

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Equipos)
admin.site.register(Servicios)
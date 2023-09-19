from django.urls import path
from Appcoder.views import *

urlpatterns =[
    #path('saluda/', saluda),
    path('agrega-curso/<nombre>/<cuit>', cliente),
    path('', Inicio, name="Inicio"),
    path('servicios/', Servicios, name="Servicios"),
    path('equipo/', Equipo, name="Equipo"),
    path('clientes/', Clientes, name="Clientes"),
    ]

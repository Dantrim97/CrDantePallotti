from django.urls import path
from Appcoder.views import *

urlpatterns =[
    #path('saluda/', saluda),
    path('agrega-curso/<nombre>/<cuit>', cliente),
    path('', Inicio),
    path('socio/', Socio),
    path('equipo/', Equipo),
    path('clientes/', Clientes),
    ]

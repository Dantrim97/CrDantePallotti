from django.urls import path
from Appcoder.views import Equipo,Clientes,AdquirirServicios,Inicio,BusquedaCliente,Busqueda
urlpatterns =[
    #path('saluda/', saluda),
    #path('agrega-curso/<nombre>/<cuit>',),
    path('', Inicio, name="Inicio"),
    #path('servicios/', Servicios, name="Servicios"),
    path('equipo/', Equipo, name="Equipo"),
    path('clientes/', Clientes, name="Clientes"),
    path('adquirir/', AdquirirServicios, name="Adquirir"),
    path('busqueda-cliente/', BusquedaCliente, name="busquedacliente"),
    path('busqueda/', Busqueda, name="busqueda"),
    ]

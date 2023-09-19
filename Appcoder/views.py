from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente
from .static import *

# Create your views here.

def cliente(req, nombre, cuit):

    cliente= Cliente(nombre=nombre, cuit=cuit)
    cliente.save()

    return HttpResponse(f"""
    <p>Cliente: {cliente.nombre} - Cuit: {cliente.cuit} creado con exito</p>
    """)


def Inicio (req):
    return render(req,"inicio.html")

def Servicios (req):
    return render(req,"Servicios.html") 

def Equipo (req):    
    return render(req,"Equipo.html")

def Clientes (req):
    return render(req,"Clientes.html")

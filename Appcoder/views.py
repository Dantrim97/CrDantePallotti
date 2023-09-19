from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .static import *

# Create your views here.

def Inicio (req):
    return render(req,"inicio.html")

#def Servicio (req):
    return render(req,"Servicios.html") 

def Equipo (req):    
    return render(req,"Equipo.html")



def Clientes(req):
    print('method', req.method)
    print('POST', req.POST)
    
    if req.method == 'POST':
        clientes = Cliente(nombre=req.POST['nombre'], cuit=req.POST['cuit'],)
        clientes.save()
        return render(req, "inicio.html")
    else:
        return render(req, "Clientes.html")
    
def AdquirirServicios(req):
    print('method', req.method)
    print('POST', req.POST)
    
    if req.method == 'POST':
        Servicio = Servicios(nombre=req.POST['nombre'], Servicio=req.POST['Servicio'], email=req.POST['email'])
        Servicio.save()
        return render(req, "inicio.html")
    else:
        return render(req, "adquirir.html")

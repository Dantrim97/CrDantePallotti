from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente

# Create your views here.

def cliente(req, nombre, cuit):

    cliente= Cliente(nombre=nombre, cuit=cuit)
    cliente.save()

    return HttpResponse(f"""
    <p>Cliente: {cliente.nombre} - Cuit: {cliente.cuit} creado con exito</p>
    """)
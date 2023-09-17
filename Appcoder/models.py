from django.db import models

# Create your models here.
class Cliente(models.Model):

    nombre= models.CharField(max_length=40)
    cuit = models.IntegerField()

class Equipo(models.Model):

    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()

class Socio(models.Model):

    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()

from django.db import models

class DeudaCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()
    estado = models.CharField(max_length=20, choices=(('Pendiente', 'Pendiente'), ('Pagada', 'Pagada')))

    def __str__(self):
        return f"Deuda de {self.cliente} - ${self.monto}"
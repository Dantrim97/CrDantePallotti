from django.db import models

# Create your models here.
class Cliente(models.Model):

    nombre= models.CharField(max_length=40)
    cuit = models.IntegerField()

class Equipo(models.Model):

    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()

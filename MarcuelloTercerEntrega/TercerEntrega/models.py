from django.db import models

# Create your models here.

class Mallas(models.Model):

    nombreModelo=models.CharField(max_length=30)
    info = models.CharField(max_length=30)
    talles = models.CharField(max_length=30)
    colores = models.CharField(max_length=30)
    
    def __str__(self):
         return f"Modelo: {self.nombreModelo}"


class RopaInterior(models.Model):
    nombreModelo= models.CharField(max_length=30)
    info= models.CharField(max_length=30)
    talles= models.CharField(max_length=30)
    colores = models.CharField(max_length=30)

    def __str__(self):
         return f"Modelo: {self.nombreModelo}"   


class Pijamas(models.Model):
    
    nombreModelo= models.CharField(max_length=30)
    inviernoverano= models.CharField(max_length=30)
    talles= models.CharField(max_length=30)
    Colores= models.CharField(max_length=30)

    def __str__(self):
         return f"Nombre: {self.nombreModelo}"

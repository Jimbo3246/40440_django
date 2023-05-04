from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=164)#Equivalente de str
    comision =models.IntegerField()#Equivalente de int

class Estudiante(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    fecha_nacimiento=models.DateField()
    email=models.EmailField()
    telefono=models.CharField(max_length=20)#Buenas practicas para este tipo de datos
    dni=models.CharField(max_length=32)
class Profesor(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    fecha_nacimiento=models.DateField()
    email=models.EmailField()
    dni=models.CharField(max_length=32)
    profesion=models.CharField(max_length=128)
    bio=models.TextField()
class Entregable(models.Model):
    nombre=models.CharField(max_length=256)
    fecha_entrega=models.DateTimeField()
    esta_aprobado=models.BooleanField(default=False) # equivalente a bool (True, False)

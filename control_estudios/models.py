from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=164)#Equivalente de str
    comision =models.IntegerField()#Equivalente de int
    def __str__(self):
        return f"{self.nombre} | {self.comision}"

class Estudiante(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    fecha_nacimiento=models.DateField(blank=True, null=True)
    email=models.EmailField(blank=True)
    telefono=models.CharField(max_length=20, blank=True)#Buenas practicas para este tipo de datos
    dni=models.CharField(max_length=32)
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"
    
class Profesor(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    fecha_nacimiento=models.DateField(blank=True)
    email=models.EmailField()
    dni=models.CharField(max_length=32)
    profesion=models.CharField(max_length=128, blank=True)
    bio=models.TextField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"
class Entregable(models.Model):
    nombre=models.CharField(max_length=256)
    fecha_entrega=models.DateTimeField()
    esta_aprobado=models.BooleanField(default=False) # equivalente a bool (True, False)

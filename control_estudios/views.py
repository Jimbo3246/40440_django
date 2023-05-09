from django.shortcuts import render, redirect
from django.urls import reverse
from control_estudios.models import *

# Create your views here.   
def listar_estudiantes(request):    
    contexto={
         "estudiantes":Estudiante.objects.all(),         
    }
    http_responde =render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_responde
def listar_cursos(request):
    contexto={
         "cursos":Curso.objects.all(),            
    }
    http_responde =render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return http_responde
def crear_curso(request):
    contexto={}
    if request.method =="POST":
        data = request.POST #Es un diccionario
        nombre=data["nombre"]
        comision=data["comision"]
        curso=Curso.objects.create(nombre=nombre, comision=comision) #lo crean solo en RAM
        curso.save() #Se guarda en la base de datos
        # Redirecciono al usuario a la lista de cursos
        url_exitosa = reverse('lista_cursos') # estudios/cursos
        return redirect(url_exitosa)
    else: #GET
           http_responde =render(
        request=request,
        template_name='control_estudios/formulario_curso_a_mano.html',
        context=contexto,
        )
    return http_responde

        
        

  
from django.shortcuts import render, redirect
from django.urls import reverse
from control_estudios.models import *
from control_estudios.forms import *

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
def crear_curso_version_1(request):
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
def crear_curso(request):
   
    if request.method =="POST":
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid():
             data = formulario.cleaned_data #es un diccionario
             nombre = data["nombre"]
             comision = data["comision"]
             curso = Curso(nombre=nombre, comision=comision)
             curso.save()
        else:
             formulario = CursoFormulario(initial=request.POST)

             
 
        url_exitosa = reverse('lista_cursos') # estudios/cursos
        return redirect(url_exitosa)
    else: #GET
           formulario = CursoFormulario()
    http_responde = render(
                        request=request,
                        template_name='control_estudios/formulario_curso.html',  
                        context={'formulario': formulario}
        )
    return http_responde
        
def buscar_cursos(request):
    if request.method == "POST":
         data = request.POST
         busqueda = data["busqueda"]
         cursos = Curso.objects.filter(comision__contains=busqueda)#Busca cualquiera que inicie con los digitos que se mencione
         contexto={
              "cursos": cursos,
         }
    http_response=render(
         request=request,
         template_name='control_estudios/lista_cursos.html',
         context=contexto,
         )
    return http_response

def eliminar_curso(request, id):    
     curso=Curso.objects.get(id=id)     
     if request.method == "POST":
        curso.delete()
        url_exitosa = reverse('lista_cursos')
        return redirect(url_exitosa)
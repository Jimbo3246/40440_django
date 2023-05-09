from django.shortcuts import render
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
    http_responde =render(
        request=request,
        template_name='control_estudios/formulario_curso_a_mano.html',
        context=contexto,
    )
    return http_responde
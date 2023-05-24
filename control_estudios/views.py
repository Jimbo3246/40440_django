from django.shortcuts import render, redirect
from django.urls import *
from django.views.generic import *#Estas librerias sirven para crear vistas basadas en clases
from control_estudios.models import *
from control_estudios.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.   
#NO USADO
"""def listar_estudiantes(request):    
    contexto={
        "estudiantes":Estudiante.objects.all(),         
    }
    http_responde =render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_responde
"""
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
@login_required
def crear_curso(request):
   
    if request.method =="POST":
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid():
             data = formulario.cleaned_data #es un diccionario
             nombre = data["nombre"]
             comision = data["comision"]
             creador=request.user
             curso = Curso(nombre=nombre, comision=comision, creador=creador)
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
def editar_curso(request, id):
    curso=Curso.objects.get(id=id)
    if request.method == "POST":
         formulario = CursoFormulario(request.POST)
         if formulario.is_valid():
              data = formulario.cleaned_data
              curso.nombre=data['nombre']
              curso.comision=data['comision']
              curso.save()
              url_exitosa=reverse('lista_cursos')
              return redirect(url_exitosa)
    else: #GET
         inicial = {
              'nombre':curso.nombre,
              'comision':curso.comision,     
         }
         formulario = CursoFormulario(initial=inicial)
    return render(
         request=request,
         template_name='control_estudios/formulario_curso.html',
         context={'formulario':formulario},
    )

#Vistas de Estudiantes
class EstudianteListView(LoginRequiredMixin, ListView):
     model=Estudiante
     template_name='control_estudios/lista_estudiantes.html'

class EstudianteCreateView(LoginRequiredMixin, CreateView):
     model =Estudiante
     fields =('apellido','nombre','email','dni')
     success_url = reverse_lazy('lista_estudiantes') #Funcion especial que le indica que no lo resuelva ahorita, que resuelva cuando sea necesario
class EstudianteDetailView(LoginRequiredMixin, DetailView):
     model = Estudiante
     success_url = reverse_lazy('lista_estudiantes')

class EstudianteDeleteView(LoginRequiredMixin, DeleteView):
     model = Estudiante
     success_url =reverse_lazy('lista_estudiantes')
class EstudianteUpdateView(LoginRequiredMixin, UpdateView):
     model = Estudiante
     fields=('apellido', 'nombre','email','dni')
     success_url = reverse_lazy('lista_estudiantes')
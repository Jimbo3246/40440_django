from django.shortcuts import render

# Create your views here.
def listar_estudiantes(request):
    contexto={
         "estudiantes":[
             {"nombre":"Jimmy","apellido":"Rivera"},
             {"nombre":"Jorge","apellido":"Torres"},
             {"nombre":"Toribia","apellido":"Matos"},
             {"nombre":"Jenifer","apellido":"Bujele"},
             {"nombre":"Ibonne","apellido":"Tenorio"},
             {"nombre":"Luisa","apellido":"lberto"},
             ]              
    }
    http_responde =render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_responde
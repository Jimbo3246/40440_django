from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
#Todas las vistas van a recibir un parametro  llamado request 
#Todas las views deben retornar un objeto que sea un httpresponse
def inicio(request):
    contexto={}
    http_responde =render(
        request=request,
        template_name='control_estudios/index.html',
        context=contexto,
    )
    return http_responde   
def saludar(request):
    saludo="Hola querido usuario"
    pagina_html=HttpResponse(saludo)
    return pagina_html
def saludar_con_fecha(request):
    hoy=datetime.now()
    saludo=f"Hola querido usuario, fecha:{hoy.day} /{hoy.month}/{hoy.year}"
    pagina_html=HttpResponse(saludo)
    return pagina_html 
def saludar_a_usuario(request, nombre):
    texto=f"Hola {nombre}"
    pagina_html=HttpResponse(texto)
    return pagina_html    
def saludar_con_html(request):
    contexto={
        "usuario":"Futuro"

    } #No colocar coma aqui pues no te correra 
    http_responde=render(

        request=request,
        template_name='control_estudios/base.html',
        context=contexto,
    ) 
    return http_responde    
    
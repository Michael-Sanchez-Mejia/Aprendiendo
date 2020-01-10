from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request): # primera vista

    Nombre= 'Tulea'
    apellido= 'Sanchez'
    apellido2='Mejia'
    hora=datetime.datetime.now()
    doc_externo= open('E:/Python/Django/aprendiendo/aprendiendo/plantillas html/primera plantilla.html')
    
    plt=Template(doc_externo.read())
    
    ctx=Context({'nombre_persona':Nombre,'apeyido':apellido,'apeyido2':apellido2,'hora':hora})
    
    documento=plt.render(ctx)
    
    doc_externo.close()

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse ('bien vas genial 2 veces')

def damefecha(request):
    fecha_actual= datetime.datetime.now()
    return HttpResponse('la fecha actual es %s')%fecha_actual





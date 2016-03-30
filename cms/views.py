from django.shortcuts import render
from django.http import HttpResponse
from models import Pages

def id_to_page(request, identificador):
    try:
        elementos = Pages.objects.get(id=int(identificador))
        http_Resp = elementos.page
    except Pages.DoesNotExist:
        http_Resp = "<h3><font color='red'>Error! El indice introducido no " +\
                    "corresponde con ningun elemento de la tabla!</font></h3>"

    return HttpResponse(http_Resp)

def name_to_page(request, recurso):
    try:
        elementos = Pages.objects.get(name=recurso)
        http_Resp = elementos.page
    except Pages.DoesNotExist:
        http_Resp = "<h3><font color='red'>Error! El recurso introducido no " +\
                    "corresponde con ningun elemento de la tabla!</font></h3>"

    return HttpResponse(http_Resp)

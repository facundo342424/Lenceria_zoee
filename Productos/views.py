from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Productos


def lista(request):
    return render (request, 'lista.html') 
def lista_Productos(_request):
    Productosr=list(Productos.objects.values())
    data={'Productos':Productos}
    return JsonResponse(data)

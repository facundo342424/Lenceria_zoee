from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Productos
from django.contrib import messages

def lista(request):
    producto_lista = Productos.objects.all()
    valor = {
        'producto_lista': producto_lista
    }
    return render(request, 'lista.html', valor)

def Guardar_producto(request):
    if request.method == 'POST':
        Nombre = request.POST['Nombre']
        Marca = request.POST['Marca']
        Precio = request.POST['Precio']
        Color = request.POST['Color']
        
        producto = Productos(Nombre=Nombre, Marca=Marca, Precio=Precio, Color=Color)
        producto.save()
        messages.success(request, '¡Producto guardado con éxito!')
    else:
        pass
    producto_lista = Productos.objects.all()
    valor = {
        'producto_lista': producto_lista
    }
    return  render(request,'lista.html',valor)


   
def Eliminar_producto(request, prod):
    producto=Productos.objects.get(id=prod)
    producto.delete()
    messages.info(request,'Producto eliminado')
    return redirect(lista)


def editar(request, prod):
    editar_producto=Productos.objects.get(id=prod)
    producto_lista=Productos.objects.all()
    valor = {
        'editar_producto':editar_producto,
        'producto_lista':producto_lista
    }
    return render(request,'lista.html',valor)
    
    


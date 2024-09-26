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


   
def borrar_prod(request, id_Producto):
    producto = Productos.objects.get(id_Producto=id_Producto)
    producto.delete()
    messages.info(request, 'Producto eliminado')
    return redirect('lista')  



def editar(request, id_Producto):
    editar_producto = Productos.objects.get(id_Producto=id_Producto)  
    producto_lista = Productos.objects.all()
    valor = {
        'editar_producto': editar_producto,
        'producto_lista': producto_lista
    }
    return render(request, 'lista.html', valor)  

    
 

def edicion(request, id_Producto):
    producto = Productos.objects.get(id_Producto=id_Producto)  

    if request.method == 'POST':
        producto.Nombre = request.POST['Nombre']
        producto.Marca = request.POST['Marca']
        producto.Precio = request.POST['Precio']
        producto.Color = request.POST['Color']
        producto.save()
        return redirect('lista')
    
    


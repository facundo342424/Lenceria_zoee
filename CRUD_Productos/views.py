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
        
        # Redireccionar a la vista de lista después de guardar el producto
        return redirect('lista')
    
    # Si no es POST, redirigir a la lista
    return redirect('lista')

def borrar_prod(request, id_Producto):
    producto = Productos.objects.get(id_Producto=id_Producto)
    producto.delete()
    messages.info(request, 'Producto eliminado')
    # Redireccionar a la lista después de eliminar el producto
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
        messages.success(request, 'Producto actualizado con éxito')
        # Redireccionar a la lista después de la edición
        return redirect('lista')
    # Si no es POST, redirigir a la lista
    return redirect('lista')

def productos(request):
    return render(request, 'productos.html')

    
    


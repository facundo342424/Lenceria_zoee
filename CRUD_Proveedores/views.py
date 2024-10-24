from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Proveedores
from django.contrib import messages

def listaprov(request):
    proveedores_lista = Proveedores.objects.all()
    valor = {
        'proveedores_lista': proveedores_lista
    }
    return render(request, 'listaprov.html', valor)

def Agregar(request):
    if request.method == 'POST':
        Nombre = request.POST['Nombre']
        Telefono = request.POST['Telefono']
        Correo_electronico= request.POST['Correo_electronico']
        Direccion = request.POST['Direccion']
        Apellido = request.POST['Apellido']
        proveedor = proveedor(Nombre=Nombre, Telefono=Telefono, Correo_electronico=Correo_electronico,Direccion=Direccion,Apellido=Apellido)
        proveedor.save()
        messages.success(request, '¡Proveedor agregado!')
        
        
        return redirect('listaprov')
    return redirect('listaprov')

def Eliminar(request, id_Proveedor):
    proveedor = Proveedores.objects.get(id_Proveedor=id_Proveedor)
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
    return redirect('lista')turn render(request,'listaprov.html')

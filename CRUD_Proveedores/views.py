from django.shortcuts import render, redirect
from .models import Proveedores
from django.contrib import messages

def proveedores(request):
    proveedor_lista = Proveedores.objects.all()
    valor = {
        'proveedor_lista': proveedor_lista
    }
    return render(request, 'proveedores.html', valor)

def Guardar_proveedor(request):
    if request.method == 'POST':
        Nombre = request.POST['Nombre']
        Apellido = request.POST['Apellido']
        Telefono = request.POST['Telefono']
        Correo_electronico = request.POST['Correo_electronico']
        Dirección = request.POST['Dirección']
        proveedor = Proveedores(Nombre=Nombre, Apellido=Apellido, Telefono=Telefono, Correo_electronico=Correo_electronico,Dirección=Dirección)
        proveedor.save()
        messages.success(request, '¡Proveedor agregado!')
        
       
        return redirect('proveedores')
    
   
    return redirect('proveedores')

def borrar_prov(request, id_Proveedor):
    proveedor = Proveedores.objects.get(id_Proveedor=id_Proveedor)
    proveedor.delete()
    messages.info(request, 'Proveedor eliminado')
   
    return redirect('proveedores')

def editar(request, id_Proveedor):
    editar_proveedor = Proveedores.objects.get(id_Proveedor=id_Proveedor)  
    proveedor_lista = Proveedores.objects.all()
    valor = {
        'editar_proveedor': editar_proveedor,
        'proveedor_lista': proveedor_lista
    }
    return render(request, 'lista.proveedores', valor)

def edicion(request, id_Proveedor):
    proveedor = Proveedores.objects.get(id_Proveedor=id_Proveedor)
    if request.method == 'POST':
        proveedor.Nombre = request.POST['Nombre']
        proveedor.Apellido = request.POST['Apellido']
        proveedor.Telefono = request.POST['Telefono']
        proveedor.Correo_electronico = request.POST['Correo_electronico']
        proveedor.Dirección = request.POST['Dirección']
        proveedor.save()
        messages.success(request, 'Producto actualizado con éxito')
        
        return redirect('proveedores')

    return redirect('proveedores')


    
    












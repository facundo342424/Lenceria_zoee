from django.shortcuts import render, redirect
from Ventas.models import Clientes
from django.contrib import messages

def clientes(request):
    cliente_lista = Clientes.objects.all()
    valor = {
        'cliente_lista': cliente_lista
    }
    return render(request, 'lista_clientes.html', valor)
     


def Añadir_cliente(request):
    if request.method == 'POST':
        Nombre = request.POST['Nombre']
        Apellido = request.POST['Apellido']
        Domicilio = request.POST['Domicilio']
        Telefono = request.POST['Telefono']  
        cliente = Clientes(Nombre=Nombre, Apellido=Apellido, Domicilio=Domicilio, Telefono=Telefono)
        cliente.save()
        messages.success(request, '¡Cliente añadido!')

        
       
        return redirect('clientes')
    
   
    return redirect('clientes')

def borrar_cliente(request, id_Cliente):
    cliente = Clientes.objects.get(id_Cliente=id_Cliente)
    cliente.delete()
    messages.info(request, 'Cliente eliminado')
   
    return redirect('clientes')

def editar(request, id_Cliente):
    editar_cliente = Clientes.objects.get(id_Cliente=id_Cliente)  
    cliente_lista = Clientes.objects.all()
    valor = {
        'editar_cliente': editar_cliente,
        'cliente_lista': cliente_lista
    }
    return render(request, 'lista.clientes', valor)

def edicion(request, id_Cliente):
    cliente = Clientes.objects.get(id_Cliente=id_Cliente)
    if request.method == 'POST':
        cliente.Nombre = request.POST['Nombre']
        cliente.Apellido = request.POST['Apellido']
        cliente.Domicilio = request.POST['Domicilio']
        cliente.Telefono = request.POST['Telefono']
        cliente.save()
        messages.success(request, 'Cliente actualizado con éxito')

        
        return redirect('clientes')

    return redirect('clientes')





from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Clientes
from django.contrib import messages

# Listar clientes
def clientes(request):
    cliente_lista = Clientes.objects.all()
    valor = {
        'cliente_lista': cliente_lista  # Asegúrate de que 'cliente_lista' esté correctamente referenciado
    }
    return render(request, 'clientes.html', valor)

# Añadir cliente
def Añadir_cliente(request):
    if request.method == 'POST':
        Nombre = request.POST.get('Nombre')
        Apellido = request.POST.get('Apellido')
        Domicilio = request.POST.get('Domicilio')
        Telefono = request.POST.get('Telefono')
        
        cliente = Clientes(Nombre=Nombre, Apellido=Apellido, Domicilio=Domicilio, Telefono=Telefono)
        cliente.save()
        messages.success(request, '¡Cliente añadido con éxito!')
        return redirect('clientes')

    return redirect('clientes')

# Eliminar cliente
def eliminar(request, id_Cliente):
    cliente = Clientes.objects.filter(id_Cliente=id_Cliente).first()
    if cliente:
        cliente.delete()
        messages.info(request, 'Cliente eliminado con éxito')
    else:
        messages.error(request, 'Cliente no encontrado')

    return redirect('clientes')

# Editar cliente
def editar(request, id_Cliente):
    editar_cliente = Clientes.objects.filter(id_Cliente=id_Cliente).first()
    if not editar_cliente:
        messages.error(request, 'Cliente no encontrado')
        return redirect('clientes')

    cliente_lista = Clientes.objects.all()
    valor = {
        'editar_cliente': editar_cliente,
        'cliente_lista': cliente_lista
    }
    return render(request, 'clientes.html', valor)

# Actualizar cliente
def edicion(request, id_Cliente):
    cliente = Clientes.objects.filter(id_Cliente=id_Cliente).first()
    if cliente and request.method == 'POST':
        cliente.Nombre = request.POST.get('Nombre', cliente.Nombre)
        cliente.Apellido = request.POST.get('Apellido', cliente.Apellido)
        cliente.Domicilio = request.POST.get('Domicilio', cliente.Domicilio)
        cliente.Telefono = request.POST.get('Telefono', cliente.Telefono)
        cliente.save()
        messages.success(request, 'Cliente actualizado con éxito')
    else:
        messages.error(request, 'No se pudo actualizar el cliente')

    return redirect('clientes')


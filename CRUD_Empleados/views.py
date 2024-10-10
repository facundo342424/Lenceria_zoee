from django.shortcuts import render, redirect, get_object_or_404
from .models import empleados
from django.contrib import messages

# Lista de empleados
def listaEmpleados(request):
    empleados_lista = empleados.objects.all()
    return render(request, 'listaEmpleados.html', {'empleados_lista': empleados_lista})

# Añadir un nuevo empleado
def Añadir_empleados(request):
    if request.method == 'POST':
        # Recogiendo los datos del formulario
        Nombre = request.POST['Nombre']
        Apellido = request.POST['Apellido']
        Telefono = request.POST['Telefono']
        correo_electronico = request.POST['correo_electronico']  
        DNI = request.POST['DNI']
        Direccion = request.POST['Direccion']
        Localidad = request.POST['Localidad']
        
        # Crear instancia del empleado y guardar
        empleado_instance = empleados(
            Nombre=Nombre, 
            Apellido=Apellido, 
            Telefono=Telefono, 
            correo_electronico=correo_electronico,
            DNI=DNI,
            Direccion=Direccion,
            Localidad=Localidad
        )
        empleado_instance.save()
        messages.success(request, 'Empleado añadido correctamente.')
    
    # Redirigir de vuelta a la lista de empleados
    return redirect('listaEmpleados')

# Borrar un empleado
def borrar_empleado(request, id_Empleado):
    # Buscar el empleado o devolver 404 si no existe
    empleado_instance = get_object_or_404(empleados, id_Empleado=id_Empleado)   
    empleado_instance.delete()  # Eliminar el empleado
    messages.info(request, 'Empleado eliminado correctamente.')
    
    # Redirigir de vuelta a la lista de empleados
    return redirect('listaEmpleados')

# Mostrar formulario de edición con los datos del empleado
def editar(request, id_Empleado):
    # Buscar el empleado o devolver 404 si no existe
    editar_empleado = get_object_or_404(empleados, id_Empleado=id_Empleado)
    
    # Renderizar la misma plantilla pero con el formulario de edición
    return render(request, 'listaEmpleados.html', {'editar_empleado': editar_empleado})

# Guardar los cambios de la edición de un empleado
def edicion(request, id_Empleado):
    # Buscar el empleado o devolver 404 si no existe
    empleado_instance = get_object_or_404(empleados, id_Empleado=id_Empleado)

    if request.method == 'POST':
        # Actualizar los campos con los datos enviados por el formulario
        empleado_instance.Nombre = request.POST['Nombre']
        empleado_instance.Apellido = request.POST['Apellido']
        empleado_instance.Telefono = request.POST['Telefono']
        empleado_instance.correo_electronico = request.POST['correo_electronico']  
        empleado_instance.DNI = request.POST['DNI']
        empleado_instance.Direccion = request.POST['Direccion']
        empleado_instance.Localidad = request.POST['Localidad']
        empleado_instance.save()  # Guardar los cambios
        messages.success(request, 'Empleado actualizado correctamente.')
    
    # Redirigir de vuelta a la lista de empleados
    return redirect('listaEmpleados')



     
    

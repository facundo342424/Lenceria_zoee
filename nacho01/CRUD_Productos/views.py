from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Productos,Stock

def lista(request):
    producto_lista = Productos.objects.all()
    return render(request, 'lista.html', {'producto_lista': producto_lista})

def Guardar_producto(request):
    if request.method == 'POST':
        Nombre = request.POST['Nombre']
        Marca = request.POST['Marca']
        Precio = request.POST['Precio']
        Color = request.POST['Color']
        Cantidad = request.POST['Cantidad']

        if Productos.objects.filter(Nombre=Nombre, Marca=Marca, Precio=Precio, Color=Color).exists():
            messages.error(request, 'Este producto ya existe.')
        else:
            producto = Productos(Nombre=Nombre, Marca=Marca, Precio=Precio, Color=Color, Cantidad=Cantidad)
            producto.save()
            messages.success(request, '¡Producto guardado con éxito!')
            return redirect('lista')

    return render(request, 'lista.html')

def borrar_prod(request, id_Producto):
    producto = Productos.objects.get(id_Producto=id_Producto)
    producto.delete()
    messages.info(request, 'Producto eliminado')
    return redirect('lista')

def editar_producto(request, id_Producto):
    editar_producto = Productos.objects.get(id_Producto=id_Producto)  
    producto_lista = Productos.objects.all()
    valor = {
        'editar_producto': editar_producto,
        'producto_lista': producto_lista
    }
    return render(request, 'lista.html', valor)

def edicion_producto(request, id_Producto):
    producto = Productos.objects.get(id_Producto=id_Producto)
    if request.method == 'POST':
        producto.Nombre = request.POST['Nombre']
        producto.Marca = request.POST['Marca']
        producto.Precio = request.POST['Precio']
        producto.Color = request.POST['Color']
        producto.save()
        messages.success(request, 'Producto actualizado con éxito')
        
        return redirect('lista')

    return redirect('lista')




def control_stock(request):
    stock_lista = Stock.objects.all()  # Obtener todos los registros de stock
    contexto = {
        'stock_lista': stock_lista
    }
    return render(request, 'control_stock.html', contexto)

# Vista para agregar un nuevo producto al stock
def Añadir_stock(request):
    if request.method == 'POST':
        Descripción = request.POST['Descripción']
        Talle = request.POST['Talle']
        Genero = request.POST['Genero']
        Color = request.POST['Color']
        Precio = request.POST['Precio']
        Cantidad = request.POST['Cantidad']

        # Verificar si el producto ya existe en el stock
        if Stock.objects.filter(Descripción=Descripción, Talle=Talle, Genero=Genero, Color=Color).exists():
            messages.warning(request, 'Este producto ya existe en el inventario.')
        else:
            # Si no existe, crear un nuevo producto y guardarlo
            stock = Stock(Descripción=Descripción, Talle=Talle, Genero=Genero, Color=Color, Precio=Precio, Cantidad=Cantidad)
            stock.save()
            messages.success(request, '¡Stock guardado con éxito!')

        # Redirigir para evitar el problema de reenvío de formulario al actualizar la página
        return redirect('control_stock')

    # Si el método no es POST, simplemente mostramos la lista de stock
    stock_lista = Stock.objects.all()
    contexto = {
        'stock_lista': stock_lista
    }
    return render(request, 'control_stock.html', contexto)

def eliminar(request, id_stock):
    stock = Stock.objects.get(id_stock=id_stock)
    stock.delete()
    messages.success(request, 'Producto eliminado con éxito.')
    return redirect('control_stock')

def editar(request, id_stock):
    try:
        editar_stock = Stock.objects.get(id_stock=id_stock)
    except Stock.DoesNotExist:
        messages.error(request, 'El stock que estás buscando no existe.')
        return redirect('control_stock')  # O la vista que corresponda
    
    stock_lista = Stock.objects.all()
    contexto = {
        'editar_stock': editar_stock,
        'stock_lista': stock_lista
    }
    return render(request, 'control_stock.html', contexto)


def edicion(request, id_stock):
    try:
        stock = Stock.objects.get(id_stock=id_stock)
    except Stock.DoesNotExist:
        messages.error(request, 'El stock que estás buscando no existe.')
        return redirect('control_stock')  # O la vista que corresponda
    
    if request.method == 'POST':
        # Actualización de los campos del stock
        stock.Descripción = request.POST['Descripción']
        stock.Talle = request.POST['Talle']
        stock.Genero = request.POST['Genero']
        stock.Color = request.POST['Color']
        stock.Precio = request.POST['Precio']
        stock.Cantidad = request.POST['Cantidad']
        stock.save()

        messages.success(request, '¡Producto actualizado con éxito!')
        return redirect('control_stock')  # Redirigir a la lista o donde sea necesario

    contexto = {
        'stock': stock
    }
    return render(request, 'control_stock.html', contexto)




 


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Productos,Stock
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from django.http import JsonResponse

def lista_productos(request):
    producto_lista = Productos.objects.all()
    return render(request, 'lista.html', {'producto_lista': producto_lista})

@login_required
def productos_venta(request): 
    productos_venta = Productos.objects.all()
    return render(request, 'productos.html', {'productos_venta': productos_venta})

def Guardar_producto(request):
    if request.method == 'POST':
        Nombre = request.POST['Nombre']
        Marca = request.POST['Marca']
        Precio = request.POST['Precio']
        Color = request.POST['Color']
        Cantidad = request.POST['Cantidad']
        imagen = request.FILES.get('imagen')

        # Si no se sube ninguna imagen, asigna una imagen predeterminada
        if not imagen:
            imagen = 'images/default-product.jpg'  # Ruta a la imagen por defecto

        if Productos.objects.filter(Nombre=Nombre, Marca=Marca, Precio=Precio, Color=Color, Cantidad=Cantidad).exists():
            messages.error(request, 'Este producto ya existe.')
        else:
            producto = Productos(
                Nombre=Nombre, 
                Marca=Marca, 
                Precio=Precio, 
                Color=Color, 
                Cantidad=Cantidad,
                imagen=imagen
            )
            producto.save()

            stock = Stock(
                Descripción=Nombre, 
                Color=Color, 
                Precio=Precio, 
                Cantidad=Cantidad,  
                id_Producto=producto 
            )
            stock.save()

            messages.success(request, '¡Producto y stock guardados con éxito!')
            return redirect('lista_productos')

    return render(request, 'lista.html')


def borrar_prod(request, id_Producto):
    producto = Productos.objects.get(id_Producto=id_Producto)
    producto.delete()
    messages.info(request, 'Producto eliminado')
    return redirect('lista_productos')

def edit_prod(request, id_Producto):
    edita_producto = Productos.objects.get(id_Producto=id_Producto)  

    producto_lista = Productos.objects.all()
    valor = {
        'edita_producto': edita_producto,
        'producto_lista': producto_lista
    }
    return render(request, 'lista.html', valor)

def edi_prod(request, id_Producto):
    producto = Productos.objects.get(id_Producto=id_Producto)
    if request.method == 'POST':
        producto.Nombre = request.POST['Nombre']
        producto.Marca = request.POST['Marca']
        producto.Precio = request.POST['Precio']
        producto.Color = request.POST['Color']
        producto.Cantidad = request.POST['Cantidad']
        producto.save()
        messages.success(request, 'Producto actualizado con éxito')
        
        return redirect('lista_productos')

    return redirect('lista_productos')




def control_stock(request):
    stock_lista = Stock.objects.all()  
    contexto = {
        'stock_lista': stock_lista
    }
    return render(request, 'control_stock.html', contexto)

def Añadir_stock(request):
    if request.method == 'POST':
        Descripción = request.POST['Descripción']
        Talle = request.POST['Talle']
        Genero = request.POST['Genero']
        Color = request.POST['Color']
        Precio = request.POST['Precio']
        Cantidad = request.POST['Cantidad']
        id_producto = request.POST['id_Producto']  # Obtener el id_Producto desde el formulario

        try:
            producto = Productos.objects.get(id=id_producto)
        except Productos.DoesNotExist:
            messages.error(request, 'El producto seleccionado no existe.')
            return redirect('control_stock')

        if Stock.objects.filter(Descripción=Descripción, Talle=Talle, Genero=Genero, Color=Color).exists():
            messages.warning(request, 'Este stock ya existe para el producto.')
        else:
            stock = Stock(
                Descripción=Descripción, 
                Talle=Talle, 
                Genero=Genero, 
                Color=Color, 
                Precio=Precio, 
                Cantidad=Cantidad,
                id_Producto=producto  # Asociar el stock con el producto
            )
            stock.save()

            messages.success(request, '¡Stock guardado con éxito!')
            return redirect('control_stock') 

    # Pasar el listado de productos al formulario para seleccionar el producto
    producto_lista = Productos.objects.all()
    contexto = {
        'producto_lista': producto_lista
    }

    return render(request, 'control_stock.html', contexto)

   

def eliminar(request, id_stock):
    stock = Stock.objects.get(id_stock=id_stock)
    
    producto = stock.id_Producto
    
    stock.delete()
    
    if not Stock.objects.filter(id_Producto=producto).exists():
        producto.delete()
        messages.success(request, 'Producto y stock eliminados con éxito.')
    else:
        messages.success(request, 'Stock eliminado con éxito.')
    
    return redirect('control_stock')  

def editar(request, id_stock):
    try:
        editar_stock = Stock.objects.get(id_stock=id_stock)
    except Stock.DoesNotExist:
        messages.error(request, 'El stock que estás buscando no existe.')
        return redirect('control_stock')  
    
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
        return redirect('control_stock') 
    
    if request.method == 'POST':
        stock.Descripción = request.POST['Descripción']
        stock.Talle = request.POST['Talle']
        stock.Genero = request.POST['Genero']
        stock.Color = request.POST['Color']
        stock.Precio = request.POST['Precio']
        stock.Cantidad = request.POST['Cantidad']
        stock.save()

        messages.success(request, '¡Producto actualizado con éxito!')
        return redirect('control_stock')  

    contexto = {
        'stock': stock
    }
    return render(request, 'control_stock.html', contexto)



def detalle_producto(request, id_Producto):
    productos = get_object_or_404(Productos, id_Producto=id_Producto)
    return render(request, 'producto_detalle.html', {'producto': productos})


def agregar_al_carrito(request, id_Producto):
    producto = get_object_or_404(Productos, id_Producto=id_Producto)
    carrito = request.session.get('carrito', {})

    if isinstance(carrito, list):
        carrito = {}
    precio = float(producto.Precio)

    if str(producto.id_Producto) in carrito:
        carrito[str(producto.id_Producto)]['cantidad'] += 1
    else:
        carrito[str(producto.id_Producto)] = {
            'nombre': producto.Nombre,
            'precio': precio,
            'cantidad': 1,
        }

    request.session['carrito'] = carrito

    total_items = sum(item['cantidad'] for item in carrito.values())

    return JsonResponse({'success': True, 'total_items': total_items})


def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = 0 
    for item in carrito.values():
        item['subtotal'] = item['precio'] * item['cantidad'] 
        total += item['subtotal']  
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})


def borrar_prod_carrito(request, id_Producto):
    carrito = request.session.get('carrito', {})
    
    if str(id_Producto) in carrito:
        if carrito[str(id_Producto)]['cantidad'] > 1:
            carrito[str(id_Producto)]['cantidad'] -= 1  # Reduce la cantidad en 1
        else:
            del carrito[str(id_Producto)]  # Si la cantidad es 1, elimina el producto del carrito

        request.session['carrito'] = carrito
        messages.info(request, 'Producto actualizado en el carrito.')
    else:
        messages.error(request, 'Producto no encontrado en el carrito.')

    return redirect('ver_carrito')



def limpiar_carrito(request):
    request.session['carrito'] = {}
    messages.success(request, 'Carrito vaciado con éxito.')
    return redirect('ver_carrito')


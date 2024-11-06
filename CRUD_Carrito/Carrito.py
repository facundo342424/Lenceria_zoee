from .models import Ventas, DetalleVenta,empleados, TipodeVenta, Productos
from django.utils import timezone
from django.db.models import Max
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.id_Producto)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "Producto_id" : producto.id_Producto,
                "Nombre" : producto.Nombreproducto,
                "acumulado" : producto.dprecio,
                "cantidad" : 1
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.Precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id_Producto)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id_Producto)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.Precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def crear_pedido(self, user):
        # Obtenemos al empleado a partir del usuario (user) logueado
        empleado = empleados.objects.get(user=user)

        # Obtener el objeto TipoPedidos con id igual a 2
        tipo_venta = TipodeVenta.objects.get(id_TipoVenta=2)
       

        # Obtener el número de pedido más alto actualmente en la base de datos
        ultima_venta = Ventas.objects.aggregate(Max('nroventa'))
        nuevo_numero_venta = ultima_venta['nroventa__max'] + 1 if ultima_venta['nroventa__max'] else 1

        venta = Ventas(id_Empleado=empleados,id_Venta=nuevo_numero_venta,id_TipoVenta=tipo_venta,dfechapedido= timezone.now().date(),iidestado=1, itotal=0)  # Crea un nuevo pedido relacionado con el empleado
        venta.save()
        print('primero')
        print(venta)

        total_venta = 0

        for item in self.carrito.values():
            producto = Productos.objects.get(id_Producto=item["Producto_id"])

            detalle_venta = DetalleVenta(id_Venta=Ventas, id_Producto=producto, cantidad_de_productos_detalle_de_ventas=item["Cantidad"], Precio=item["acumulado"])
            detalle_venta.save()
            total_venta += item["acumulado"]

        venta.total = total_venta
        venta.save()
        print('segundo')
        print(venta)

        # Limpia el carrito después de crear el pedido
        self.limpiar()
        return venta # Añade esta línea para retornar el pedido creado
        

   
from .Carrito import Carrito
from CRUD_Carrito.models import Productos, DetalleVenta
from django.views.generic import TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

###########begin debugg consola###################
import logging

# Configuración del registro
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Configuración del controlador para la consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
###########end debugg consola###################

class Tienda(TemplateView):
    template_name = 'tienda.html'

    def dispatch(self, request, *args, **kwargs):
        # Verifica si el usuario está autenticado
        if not request.user.is_authenticated:
            return redirect('login')

        # Verifica si el usuario pertenece a uno de los grupos requeridos
        if not request.user.groups.filter(name__in=['Administrador', 'Operador', 'Usuario']).exists():
            return redirect('login')  # Redirige si no pertenece a los grupos requeridos

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Productos.objects.all()  # Obtiene todos los productos
        context['title'] = 'Carrito de Compras'
        return context

def agregar_producto(request, producto_id):
    if not request.user.is_authenticated:
        return redirect('login')
    carrito = Carrito(request)
    producto = get_object_or_404(Productos, iidproducto=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    if not request.user.is_authenticated:
        return redirect('login')
    carrito = Carrito(request)
    producto = get_object_or_404(Productos, iidproducto=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    if not request.user.is_authenticated:
        return redirect('login')
    carrito = Carrito(request)
    producto = get_object_or_404(Productos, iidproducto=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    if not request.user.is_authenticated:
        return redirect('login')
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")

def render_pdf(template_path, context_dict):
    template = get_template(template_path)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding="UTF-8")

    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="comprobante_venta.pdf"'
        return response

    return HttpResponse("Error al generar el PDF", content_type='text/plain')

def confirmar_pedido(request):
    if not request.user.is_authenticated:
        return redirect('login')
    carrito = Carrito(request)
    venta = carrito.crear_pedido(request.user)  # Crear el pedido y recibirlo
    detalle_venta = DetalleVenta.objects.filter(id_Venta=venta)  # Obtener detalles del pedido
    total = 0  # Inicializa una variable para el total

    for detalle in detalle_venta:
        detalle.acumulado = detalle.cantidad_de_productos_detalle_de_ventas * detalle.precio_unitario_venta
        total += detalle.acumulado
    
    contexto = {
        'venta': venta,
        'detalle_venta': detalle_venta,
        'total': total,
    }
    # Llama a la función render_pdf para generar el PDF
    pdf = render_pdf('comprobante_venta.html', contexto)
    return pdf

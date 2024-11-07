from .Carrito import Carrito
from CRUD_Carrito.models import Productos, DetalleVenta
from django.views.generic import TemplateView
from loguinApp.mixins import AuthGroupRequiredMixin
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
###########begin debugg consola###################

# se importa solo pra mostrar los logger en la consola de ejecucion
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

# def usuario_puede_modificar_carrito(user):
#     return user.groups.filter(name__in=['Administrador', 'Operador']).exists()

class Tienda(AuthGroupRequiredMixin, TemplateView):
    template_name = 'Tienda.html'
    groups_required = ['Administrador','Operador','Usuario']

class Productos(AuthGroupRequiredMixin,TemplateView):
    template_name='lista.html'
    groups_required=['Usuario']
      


    def dispatch(self, request, *args, **kwargs):
        #logger.debug("Entrando al método dispatch")
        user = self.request.user
        #logger.debug(f"Grupos del usuario: {user.groups.all()}")
        result = super().dispatch(request, *args, **kwargs)
        #logger.debug("Saliendo del método dispatch")
        return result
    
    #######end: codigo necesario solo para ver la salida del mixins en consola####

    def get_context_data(self, **kwargs):
        print("Eget contxt")
        context = super().get_context_data(**kwargs)
        # Agrega el modelo de productos al contexto
        context['productos'] = Productos.objects.all()  # Esto obtendrá todos los productos  
        # Puedes agregar cualquier otro contexto que desees aquí
        context['title'] = 'Carrito de Compras'
        return context
    
#@user_passes_test(lambda u: u.groups.filter(name__in=['Administrador', 'Operador']).exists(), login_url=reverse_lazy('login'))
def agregar_producto(request,id_Producto):
    carrito = Carrito(request)
    producto = Productos.objects.get(id_Producto=id_Producto)
    carrito.agregar(producto)
    return redirect("Tienda")

#@user_passes_test(lambda u: u.groups.filter(name__in=['Administrador', 'Operador']).exists(), login_url=reverse_lazy('login'))
def eliminar_producto(request,id_Producto):
    carrito = Carrito(request)
    producto = Productos.objects.get(id_Producto=id_Producto)
    carrito.eliminar(producto)
    
#@user_passes_test(lambda u: u.groups.filter(name__in=['Administrador', 'Operador']).exists(), login_url=reverse_lazy('login'))
def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(iidproducto=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

#@user_passes_test(lambda u: u.groups.filter(name__in=['Administrador', 'Operador']).exists(), login_url=reverse_lazy('login'))
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")

# def render_pdf(template_path, context_dict):
#     template = get_template(template_path)
#     html = template.render(context_dict)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="comprobante_venta.pdf"'

#     # Crear el PDF a partir de la plantilla HTML
#     pisa.CreatePDF(html, dest=response)
#     return response
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
    carrito = Carrito(request)
    pedido = carrito.crear_pedido(request.user)  # Crear el pedido y recibirlo
    detalle_pedido = DetalleVenta.objects.filter(id_Venta=pedido)  # Obtener detalles del pedido
    total = 0  # Inicializa una variable para el total

    for detalle in detalle_pedido:
        detalle.acumulado = detalle.icantidad * detalle.precio_unitario
        total += detalle.acumulado
    
    contexto = {
        'pedido': pedido,
        'detalle_pedido': detalle_pedido,
        'total': total,
    }
    # Llama a la función render_pdf para generar el PDF
    pdf = render_pdf('comprobante_venta.html', contexto)
    return pdf

    # Renderiza la página HTML usando la función render
    #return render(request, 'comprobante_venta.html', contexto)
    
    

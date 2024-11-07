from django.shortcuts import render, redirect
from CRUD_Carrito.models import caja, empleados
# from CarritoApp.models import Empleados
# from CarritoApp.models import Sucursales
from django.views.generic import TemplateView
from loguinApp.mixins import AuthGroupRequiredMixin
from django.utils import timezone
#from django.http import JsonResponse
import json
from .forms import CajasForm
from django.http import HttpResponse

# Create your views here.
class administrarCajas(AuthGroupRequiredMixin, TemplateView):
    template_name = 'cajas.html'
    groups_required = ['Administrador','Operador']  # Lista de grupos requeridos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        cajas = caja.objects.all().values('numero', 'Monto_inicial_Caja', 'id_caja')
        cajas_serializados = []
        for caja in cajas:
            cajas_serializados.append({
                'numero': caja['inrocaja'],
                'Monto_inicial_Caja': float(caja['Monto_inicial_Caja']),
                'id_caja': caja['id_caja'],
            })
        context['title'] = 'Administración de Cajas'

        fecha_actual = timezone.now().date() #.strftime('%Y-%m-%d')       
       
        # Realiza la consulta y filtra en Python
        objetos = caja.objects.filter(dfechacierre__isnull=True)
        
        caja_abierta = [objeto for objeto in objetos if objeto.Fecha_apertura_caja.date() == fecha_actual]    

        context ['estado_caja'] = caja_abierta
        test_all = json.dumps({'cajas': list(cajas_serializados)})        
     
        context['test_data'] = test_all        
        
        return context
    
def abrirCaja(request):    
    
    if request.user.is_authenticated:
        user_id = request.user.id  # Obtiene el user_id del usuario autenticado
        try:
            empleado = empleados.objects.get(user_id=user_id)  # Busca el empleado por user_id
            # Ahora tienes el empleado, puedes utilizarlo como sea necesario
        except empleados.DoesNotExist:
            # Maneja el caso en el que no se encuentra un empleado para este usuario
            empleado = None
    else:
        empleado = None  # Opcional: Manejo si el usuario no está autenticado

    if request.method == 'POST':
        form = CajasForm(request.user, request.POST)
        if form.is_valid():
            form.save()
          
            response = HttpResponse("<section class='vh-100 d-flex justify-content-center align-items-center'><h2>caja abierta, puedes operar</h2></section>")
         
            return response
            #return redirect('administrarCajas')
    else:
        form = CajasForm(user=request.user)  # Pasa el usuario al formulario

    return render(request,"abrirCaja.html", {'form': form})


# from django.http import JsonResponse
# from .models import Cajas

# def api_items(request):
#     items = Cajas.objects.all()
#     data = [{'nro': item.inrocaja, 'monto': item.fmontoapertura} for item in items]
#     return JsonResponse(data, safe=False)
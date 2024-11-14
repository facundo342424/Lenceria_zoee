from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from CRUD_Carrito.models import Clientes
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ClienteForm

class ClienteListView(View):
    def get(self, request):
        # Verificar si la solicitud es AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            clientes = Clientes.objects.all().values('id_Cliente', 'Nombre', 'Apellido', 'Domicilio','Telefono')
            clientes_list = list(clientes)
            return JsonResponse({'data': clientes_list})
        # Título para la página
        title = "Bienvenido a mi sitio"
        # Contexto para la plantilla HTML
        context = {
            'title': title,
        }
        # Renderizar la plantilla HTML para solicitudes normales
        return render(request, 'listClientes.html', context)


class ClienteCreateView(CreateView):
    model = Clientes
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('api_clientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Cliente'
        return context

    def form_valid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form.save()
            return JsonResponse({'form_is_valid': True})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'form_is_valid': False, 'html_form': render(self.request, self.template_name, {'form': form}).content.decode()})
        return super().form_invalid(form)


class ClienteUpdateView(UpdateView):
    model = Clientes
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('api_clientes')

    def form_valid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form.save()
            return JsonResponse({'form_is_valid': True})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'form_is_valid': False, 'html_form': render(self.request, self.template_name, {'form': form}).content.decode()})
        return super().form_invalid(form)

class ClienteDeleteView(DeleteView):
    model = Clientes
    template_name = 'cliente_confirm_delete.html'
    success_url = reverse_lazy('api_clientes')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'form_is_valid': True})
        return response

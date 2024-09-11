# views.py
from django.views.generic import ListView, CreateView,  DeleteView
from .models import Productos

class ProductListView(ListView):
    model = Productos
    template_name = 'lista.html'

class ProductCreateView(CreateView):
    model = Productos
    template_name = 'formulario.html'
    success_url = '/productos/'

class ProductDeleteView(DeleteView):
    model = Productos
    template_name = 'borrar.html'
    success_url = '/productos/'

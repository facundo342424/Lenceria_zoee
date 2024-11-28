from django import forms
from .models import Ventas

class VentaForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = [ 'Fecha_venta', 'Total_venta','Nombre_de_tipo_de_venta','Descripción','Dni','Nombre','']
    
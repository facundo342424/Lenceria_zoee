
from django import forms
from Ventas.models import Clientes

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [ 'Nombre', 'Apellido', 'Domicilio','Telefono']

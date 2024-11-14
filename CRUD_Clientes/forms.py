from django import forms
from CRUD_Carrito.models import Clientes

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['id_Cliente','Nombre','Apellido','Domicilio','Telefono'] 
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Apellido': forms.EmailInput(attrs={'class': 'form-control'}),
        }
         
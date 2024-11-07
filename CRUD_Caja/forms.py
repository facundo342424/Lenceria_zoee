from django import forms
from django.forms import ModelForm
from CRUD_Carrito.models import caja,empleados
from django.utils import timezone


class CajasForm(ModelForm):
    
    fechaapertura = forms.DateTimeField(initial=timezone.now, label='Fecha y Hora de Apertura',required=True)
   
    class Meta:
        model = caja
        fields = ['numero','Fecha_apertura_caja','Fecha_cierre_caja', 'Monto_inicial_Caja']
        exclude = ['Fecha_apertura_caja', 'Fecha_cierre_caja']  

    def __init__(self, user, *args, **kwargs):
        super(CajasForm, self).__init__(*args, **kwargs)
        self.user = user  

    def save(self, commit=True):
        # Obtén el empleado correspondiente al usuario
        empleado = empleados.objects.get(user=self.user)
        
        # Crea una nueva instancia de Cajas y establece el empleado
        instance = super(CajasForm, self).save(commit=False)
        instance.id_Empleado = empleado

        if commit:
            instance.save()

        return instance
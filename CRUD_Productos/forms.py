# forms.py
from django import forms
from models import Productos,Stock

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['id_Producto', 'Nombre', 'Marca', 'Precio','Color','Cantidad']
class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['id_stock','Descripción', 'Talle', 'Genero','Color','Precio','Cantidad']
    
        
  
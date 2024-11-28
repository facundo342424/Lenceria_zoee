import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
from django.http import HttpResponse

def Control_producto(request):
    # Datos de ejemplo (cambiar por datos reales)
    productos = ['buzo_overside', 'remera negra', 'Pantalon']
    ventas = [50, 75, 100]
    
    # Crear el gráfico de barras
    plt.figure(figsize=(8, 5))
    plt.bar(productos, ventas, color=['blue', 'orange', 'green'])
    plt.title('Ventas de Productos')
    plt.xlabel('Productos')
    plt.ylabel('Cantidad Vendida')
    plt.tight_layout()
    
    # Convertir el gráfico en una imagen para incrustar en HTML
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    
    # Renderizar el gráfico en la plantilla
    context = {
        'grafico': image_base64
    }
    return render(request, 'productos_stock.html', context)

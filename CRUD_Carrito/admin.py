from django.contrib import admin
from CRUD_Carrito.models import empleados, Productos, Stock

@admin.register(empleados)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ["upper_case_name", "upper_case_apellido", "documento", "usuario"]
    search_fields = ["Nombre", "Apellido"]
    list_per_page = 5
    list_select_related = True

    @admin.display(description="Nombre")
    def upper_case_name(self, obj):
        return obj.Nombre.upper()

    @admin.display(description="Apellido")
    def upper_case_apellido(self, obj):
        return obj.Apellido.upper()

    @admin.display(description="Documento")
    def documento(self, obj):
        return obj.DNI

    def usuario(self, obj):
        return obj.user.username

@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ["Nombre", "Marca", "Precio", "Color"]  # Asegúrate de que estos atributos existan

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ["id_Producto", "disponible_stock"]  # Usa 'disponible_stock' en minúsculas


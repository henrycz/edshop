from django.contrib import admin
from .models import Categoria, Producto
# Clasico
admin.site.register(Categoria)
# admin.site.register(Producto)

# Usando decorador
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # List_display=Campos que deseas que se muestre en el listado. Siempre se usa duplas (siempre con comas).
    list_display = ('nombre', 'precio', 'categoria', 'fecha_registro')
    list_editable = ('precio',)

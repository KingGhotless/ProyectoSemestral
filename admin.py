from django.contrib import admin
from .models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','stock','descripcion','tipo','imagen']
    search_fields = ['codigo','nombre']

admin.site.register(tipoProducto)
admin.site.register(Producto,ProductoAdmin)
from distutils.command.upload import upload
from django.db import models

# Create your models here.

class tipoProducto(models.Model):
    tipo = models.CharField(max_length=20)
    
    def __str__(self):
        return self.tipo
    
    class Meta:
       db_table = 'db_tipo_producto'

class Producto(models.Model):
    codigo = models.IntegerField(null=False,primary_key=True)
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=20)
    tipo = models.ForeignKey(tipoProducto,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_producto'
        
# CARRITO

class items_carrito(models.Model):
    nombre_producto = models.CharField(max_length=40)
    precio_producto = models.IntegerField()
    imagen = models.ImageField(upload_to="items_carrito", null=True)
    
    def __str__ (self):
        return self.nombre_producto
    
    class Meta:
        db_table = 'db_items_carrito'
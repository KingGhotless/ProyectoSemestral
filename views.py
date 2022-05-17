from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

# SECCION LISTAR

def index(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    
    if request.method == 'POST':
        
        tipo = tipoProducto()
        tipo.tipo = request.POST.get('tipo')
        
        producto = Producto()
        producto.codigo = request.POST.get('codigo')
        producto.nombre = request.POST.get('nombre')
        producto.marca = request.POST.get('marca')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.descripcion = request.POST.get('descripcion')
        producto.imagen = request.POST.get('imagen')
        
        carrito = items_carrito()
        carrito.producto = producto
        carrito.save()
        
        carrito = items_carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()

    return render(request, 'app/index.html', datos)

def carrito(request):
    return render(request, 'app/carrito.html')

def carritoPremium(request):
    return render(request, 'app/carritoPremium.html')

def estadoPedido(request):
    return render(request, 'app/estadoPedido.html')

def estadoPedidoPremium(request):
    return render(request, 'app/estadoPedidoPremium.html')

def help(request):
    return render(request, 'app/help.html')

def historial(request):
    return render(request, 'app/historial.html')

def historialPremium(request):
    return render(request, 'app/historialPremium.html')

def indexUsu(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    
    if request.method == 'POST':
        
        tipo = tipoProducto()
        tipo.tipo = request.POST.get('tipo')
        
        producto = Producto()
        producto.codigo = request.POST.get('codigo')
        producto.nombre = request.POST.get('nombre')
        producto.marca = request.POST.get('marca')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.descripcion = request.POST.get('descripcion')
        producto.imagen = request.POST.get('imagen')
        
        carrito = items_carrito()
        carrito.producto = producto
        carrito.save()
        
        carrito = items_carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()
        
    return render(request, 'app/indexUsu.html', datos)

def indexSuscrip(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    
    if request.method == 'POST':
        
        tipo = tipoProducto()
        tipo.tipo = request.POST.get('tipo')
        
        producto = Producto()
        producto.codigo = request.POST.get('codigo')
        producto.nombre = request.POST.get('nombre')
        producto.marca = request.POST.get('marca')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.descripcion = request.POST.get('descripcion')
        producto.imagen = request.POST.get('imagen')
        
        carrito = items_carrito()
        carrito.producto = producto
        carrito.save()
        
        carrito = items_carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()
    
    return render(request, 'app/indexSuscrip.html', datos)

def prodGatoBandana(request):
    return render(request, 'app/prodGatoBandana.html')

def prodGatoBandanaPremium(request):
    return render(request, 'app/prodGatoBandanaPremium.html')

def prodGatoCorrea(request):
    return render(request, 'app/prodGatoCorrea.html')

def prodGatoCorreaPremium(request):
    return render(request, 'app/prodGatoCorreaPremium.html')

def prodGatoId(request):
    return render(request, 'app/prodGatoId.html')

def prodGatoIdPremium(request):
    return render(request, 'app/prodGatoIdPremium.html')

def prodPerroBandana(request):
    return render(request, 'app/prodPerroBandana.html')

def prodPerroBandanaPremium(request):
    return render(request, 'app/prodPerroBandanaPremium.html')

def prodPerroCorrea(request):
    return render(request, 'app/prodPerroCorrea.html')

def prodPerroCorreaPremium(request):
    return render(request, 'app/prodPerroCorreaPremium.html')

def prodPerroId(request):
    return render(request, 'app/prodPerroId.html')

def prodPerroIdPremium(request):
    return render(request, 'app/prodPerroIdPremium.html')

# SECCION AGREGAR CON FORMULARIO

def agregar_producto(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST' :
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto guardado correctamente!"
        
    return render(request, 'app/productos/agregar_producto.html', datos)

# seccion modificar (con codigo)

def modificar_producto (request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=Producto)
    }
    if request.method == 'POST':
        producto = Producto
        producto.nombre = request.POST.get('txtNombre')
        producto.save()

    return render(request, 'app/productos/modificar_producto.html', datos)

# seccion listar

def listar_producto(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request, 'app/productos/listar_producto.html',datos)

# seccion eliminar

def eliminar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listar_producto")
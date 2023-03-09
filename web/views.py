from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Producto
from .carrito import Cart
# VISTAS PARA EL CATALOGO DE PRODUCTOS

def index(request):
    listaproductos = Producto.objects.all()
    listaCategorias = Categoria.objects.all()

    context = {
        'productos': listaproductos,
        'categorias': listaCategorias
    }
    return render(request, 'index.html', context)


# VISTAS PARA FILTRAR PRODUCTOS POR CATEGORIA
def productosPorCategoria(request, categoria_id):
    objCategoria = Categoria.objects.get(pk=categoria_id)

    listaproductos = objCategoria.producto_set.all()
    listaCategorias = Categoria.objects.all()

    context = {
        'categorias': listaCategorias,
        'productos': listaproductos
    }

    return render(request, 'index.html', context)


# VISTAS PARA FILTRAR PRODUCTOS POR CATEGORIA
def productosPorNombre(request):
    nombrex = request.POST['nombre']
    # nombre__contains = Que sea igual a la variable nombre que se esta pasando.
    listaproductos = Producto.objects.filter(nombre__contains=nombrex)
    listaCategorias = Categoria.objects.all()

    context = {
        'categorias': listaCategorias,
        'productos': listaproductos
    }

    return render(request, 'index.html', context)


# VISTAS PARA LOS DETALLES DEL PRODUCTO
def productoDetalle(request, producto_id):

    # objProducto = Producto.objects.get(pk=producto_id)
    objProducto = get_object_or_404(Producto, pk=producto_id)
    context = {
        'producto': objProducto
    }

    return render(request, 'producto.html', context)


# VISTAS PARA CARRITO DE COMPRAS
def carrito(request):
    return render(request, 'carrito.html')

def agregarCarrito(request, producto_id):
    if request.method != 'POST':
        cantidad = 1
    else:
        cantidad = int(request.POST['cantidad'])

    objProducto = Producto.objects.get(pk=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto, cantidad)
    # print para saber si esta viajando las variables del carrito.
    # print(request.session.get("cart"))
    # para que agregar al carrito sin pasar a otra pagina.
    if request.method == 'GET':
        return redirect('/')

    return render(request, 'carrito.html')

def eliminarProductoCarrito(request, producto_id):
    objProducto = Producto.objects.get(pk=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.delete(objProducto)

    return render(request, 'carrito.html')

def limpiarCarrito(request):
    carritoProducto = Cart(request)
    carritoProducto.clear()

    return render(request, 'carrito.html')








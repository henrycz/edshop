from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto
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


def productoDetalle(request, producto_id):

    # objProducto = Producto.objects.get(pk=producto_id)
    objProducto = get_object_or_404(Producto, pk=producto_id)
    context = {
        'producto': objProducto,
    }

    return render(request, 'producto.html', context)



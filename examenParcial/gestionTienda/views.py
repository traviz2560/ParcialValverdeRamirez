from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
import json

from .models import Tienda, Producto
from .forms import TiendaForm, ProductoForm

# views tienda.
def tiendas(request):
    return render(request, 'tiendas.html')

def listaTienda(request):
    tiendas = Tienda.objects.all()
    return render(request, "listaTienda.html", {
        'tiendas': tiendas
    })

def listaTiendaFiltro(request, pk):
    tienda = get_object_or_404(Tienda, pk=pk)
    try:
        productos = Producto.objects.filter(tiendaRelacionada=tienda)
    except:
        productos = None
    return render(request, "listaProducto.html", {
        'productos': productos
    })

def agregarTienda(request):
    if request.method == 'POST':
        form = TiendaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        'listaTiendaCambio': None,
                    })
                }
            )
    else:
        form = TiendaForm()
    return render(request, 'tiendaForm.html', {'form':form})

def editarTienda(request, pk):
    tienda = get_object_or_404(Tienda, pk=pk)
    if request.method == "POST":
        form = TiendaForm(request.POST, instance=tienda)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        'listaTiendaCambio': None,
                    })
                }
            )
    else:
        form = TiendaForm(instance=tienda)
    return render(request, 'tiendaForm.html', {
        'form': form,
        'tienda': tienda,
    })

def eliminarTiendas(request):
    print(request)
    if request.method == 'POST':
        Tienda.objects.all().delete()
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    'listaTiendaCambio': None,
                })
            }
        )
    return render(request, 'borrarTiendaForm.html')

def detalleTienda(request, pk):
    tienda = get_object_or_404(Tienda, pk=pk)
    return render(request, 'detalleTienda.html', {
        'tienda':tienda,
    })

@ require_POST
def eliminarTienda(request, pk):
    tienda = get_object_or_404(Tienda, pk=pk)
    tienda.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                'listaTiendaCambio': None,
            })
        })

# views producto.
def productos(request):
    return render(request, 'productos.html')

def listaProducto(request):
    productos = Producto.objects.all()
    return render(request, "listaProducto.html", {
        'productos': productos
    })

def agregarProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        'listaProductoCambio': None,
                    })
                }
            )
    else:
        form = ProductoForm()
    return render(request, 'productoForm.html', {'form':form})

def editarProducto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        'listaProductoCambio': None,
                    })
                }
            )
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productoForm.html', {
        'form': form,
        'producto': producto,
    })

def eliminarProductos(request):
    print(request)
    if request.method == 'POST':
        Producto.objects.all().delete()
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    'listaProductoCambio': None,
                })
            }
        )
    return render(request, 'borrarProductoForm.html')

@ require_POST
def eliminarProducto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                'listaProductoCambio': None,
            })
        })
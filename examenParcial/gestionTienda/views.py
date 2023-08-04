from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json

from .models import Tienda, Producto
from .forms import TiendaForm, ProductoForm

# Create your views here.
def tiendas(request):
    return render(request, 'tiendas.html')

def productos(request):
    return render(request, 'productos.html')

def listaTienda(request):
    return render(request, "listaTienda.html", {
        'tiendas': Tienda.objects.all()
    })

def listaProducto(request):
    return render(request, "listaProducto.html", {
        'productos': Producto.objects.all()
    })

def agregarTienda(request):
    if request.method == 'POST':
        form = TiendaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': 'listaTiendaCambio'
                }
            )
    else:
        form = TiendaForm()
    return render(request, 'tiendaForm.html', {'form':form})

def agregarProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': 'listaProductoCambio'
                }
            )
    else:
        form = TiendaForm()
    return render(request, 'productoForm.html', {'form':form})
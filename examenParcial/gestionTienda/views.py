from django.shortcuts import render
from django.http import HttpResponse
from .models import Tienda, Producto

# Create your views here.
def productos(request):
    return render(request, 'productos.html')

def tiendas(request):
    return render(request, 'tiendas.html')

def agregarProductosyTiendas(request):
    return render(request, 'agregar.html')

def detalleTiendas(request):
    return render(request, 'detalles.html')
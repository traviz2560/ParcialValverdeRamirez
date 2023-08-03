from django.shortcuts import render
from django.http import HttpResponse
from .models import Tienda, Producto
from django.template import loader

# Create your views here.
def tiendas(request):
    template = loader.get_template('tiendas.html')
    context = {}
    return HttpResponse(template.render(context, request))

def productos(request):
    template = loader.get_template('productos.html')
    context = {}
    return HttpResponse(template.render(context, request))
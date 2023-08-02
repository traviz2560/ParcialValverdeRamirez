from django.urls import path
from . import views

app_name = 'gestionTienda'

urlpatterns = [
    path('', views.productos, name='productos'),
    path('tiendas/', views.tiendas, name='tiendas'),
    path('agregar/', views.agregarProductosyTiendas, name='agregarProductosyTiendas'),
    path('detalle/', views.detalleTiendas, name='detalleTiendas'),
]
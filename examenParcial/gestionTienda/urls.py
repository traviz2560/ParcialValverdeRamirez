from django.urls import path
from . import views

app_name = 'gestionTienda'

urlpatterns = [
    path('gestionTienda/', views.tiendas, name='tiendas'),
    path('gestionTienda/lista', views.listaTienda, name='listaTienda'),
    path('gestionTienda/agregar', views.agregarTienda, name='agregarTienda'),
    path('gestionTienda/Productos/', views.productos, name='productos'),
    path('gestionTienda/Productos/agregar', views.agregarProducto, name='agregarProducto'),
    path('gestionTienda/Productos/lista', views.listaProducto, name='listaProducto'),
]
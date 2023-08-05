from django.urls import path
from . import views

app_name = 'gestionTienda'

urlpatterns = [
    path('gestionTienda/', views.tiendas, name='tiendas'),
    path('gestionTienda/lista', views.listaTienda, name='listaTienda'),
    path('gestionTienda/agregar', views.agregarTienda, name='agregarTienda'),
    path('gestionTienda/<int:pk>/editar', views.editarTienda, name='editarTienda'),
    path('gestionTienda/<int:pk>/eliminar', views.eliminarTienda, name='eliminarTienda'),
    path('gestionTienda/limpiar', views.eliminarTiendas, name='eliminarTiendas'),
    path('gestionTienda/<int:pk>/detalles/', views.detalleTienda, name='detalleTienda'),
    path('gestionTienda/<int:pk>/detalles/lista', views.listaTiendaFiltro, name='listaTiendaFiltro'),
    path('gestionTienda/Productos/', views.productos, name='productos'),
    path('gestionTienda/Productos/lista', views.listaProducto, name='listaProducto'),
    path('gestionTienda/Productos/agregar', views.agregarProducto, name='agregarProducto'),
    path('gestionTienda/Productos/<int:pk>/editar', views.editarProducto, name='editarProducto'),
    path('gestionTienda/Productos/<int:pk>/eliminar', views.eliminarProducto, name='eliminarProducto'),
    path('gestionTienda/Productos/limpiar', views.eliminarProductos, name='eliminarProductos'),
]
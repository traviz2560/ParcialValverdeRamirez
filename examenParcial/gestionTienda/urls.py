from django.urls import path
from . import views

app_name = 'gestionTienda'

urlpatterns = [
    path('gestionTienda/', views.tiendas, name='tiendas'),
    path('gestionTienda/Productos/', views.productos, name='productos'),
]
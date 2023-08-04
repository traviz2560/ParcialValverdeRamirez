from django import forms
from .models import Tienda, Producto

class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = ['direccion', 'provincia', 'region', 'fechaCreacion', 'telefono']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['descripcion', 'codigo', 'precioVenta', 'cantidad', 'tiendaRelacionada']
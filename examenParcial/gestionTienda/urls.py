from django.urls import path
from . import views

app_name = 'gestionTienda'

urlpatterns = [
    path('members/', views.members, name='members'),
]
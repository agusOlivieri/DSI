from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('vinos/', views.vinos),
    path('ver_actualizaciones/', views.verJson),
    path('crear_bodega/', views.actualizar_vinos),
]
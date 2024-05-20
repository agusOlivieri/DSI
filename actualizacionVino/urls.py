from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ver_actualizaciones/', views.verActualizaciones),
    path('actualizar/actualizar_vino', views.actualizarVino),
    path('actualizar/crear_vino', views.crearVino),
]
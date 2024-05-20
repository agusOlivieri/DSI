from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('actualizar/', views.verActualizaciones),
    path('actualizar/actualizar_vino/<int:id>', views.actualizarVino),
    # path('actualizar/crear_vino/<int:id>', views.crearVino),
]
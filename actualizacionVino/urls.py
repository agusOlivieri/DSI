from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('actualizar/', views.verActualizaciones),
    path('actualizar/actualizar_vino', views.actualizarVino),
    # path('actualizar/crear_vino', views.crearVino),
    path('actualizar/crear_vino/<int:id>', views.crearVino),
]
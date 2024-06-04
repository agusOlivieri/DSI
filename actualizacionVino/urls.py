from django.urls import path
from .controlers import GestorImportarActualizaciones
from .views import PantallaImportarActualizaciones, index
from .inicializador import inicializar

urlpatterns = [
    path('', index),
    path('crear/', inicializar),
    path('actualizar/', PantallaImportarActualizaciones.opImportarActualizacionVinos),
    path('actualizar/actualizar_vino/<str:nombre>', PantallaImportarActualizaciones.tomarSeleccionBodega),
]
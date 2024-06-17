from django.shortcuts import render

from .models import *
from .controlers import GestorImportarActualizaciones

# Create your views here.

class PantallaImportarActualizaciones:
    
    def opImportarActualizacionVinos(request):
        return PantallaImportarActualizaciones.habilitar(request)

    def habilitar(request):
        return GestorImportarActualizaciones.opImportarActualizacionVinos(request)
  
    def mostrarBodegasParaActualizar(request, bodegasParaActualizar):
        return render(request, 'bodegas_para_actualizar.html', {
            'bodegas': bodegasParaActualizar
        })
    
    def tomarSeleccionBodega(request, nombreBodega):
        return GestorImportarActualizaciones.tomarSeleccionBodega(request, nombreBodega)

    def mostrarResumenVinosImportados(request, vinosImportados, nombreBod, notif):
        return render(request, 'vinos_importados.html', {
            'vinosImportados': vinosImportados,
            'bodega': nombreBod,
            'notificacion': notif
        })

def index(request): 
    return render(request, 'index.html')

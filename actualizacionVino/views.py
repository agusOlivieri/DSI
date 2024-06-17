from django.shortcuts import render

from .models import *
from .controlers import GestorImportarActualizaciones

# Create your views here.

class PantallaImportarActualizaciones:
    
    def opImportarActualizacionVinos(request):
        return PantallaImportarActualizaciones.habilitar(request)

    def habilitar(request):
        return GestorImportarActualizaciones.opImportarActualizacionVinos(request)
        # return PantallaImportarActualizaciones.mostrarBodegasParaActualizar(request, listaBodegasParaActualizar)
  
    def mostrarBodegasParaActualizar(request, bodegasParaActualizar):
        return render(request, 'bodegas_para_actualizar.html', {
            'bodegas': bodegasParaActualizar
        })
    
    def tomarSeleccionBodega(request, nombre):
        return GestorImportarActualizaciones.tomarSeleccionBodega(request, nombre)
        
        # return PantallaImportarActualizaciones.mostrarResumenVinosImportados(request, actualizaciones, nombre)
        
    def mostrarResumenVinosImportados(request, actualizaciones, nombreBod, notif):
        return render(request, 'vinos_importados.html', {
            'actualizaciones': actualizaciones,
            'bodega': nombreBod,
            'notificacion': notif
        })

    def mostrarConfirmacionDeNotificacion(request, confirmacion):
        return render(request, )

def index(request): 
    return render(request, 'index.html')


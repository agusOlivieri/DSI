from django.shortcuts import render

from .interfaces import *
from .models import *

class GestorImportarActualizaciones:
    seleccionBodega = None
    tipoUva = None
    maridaje = None
    listaSeguidoresDeBodega = []
    datosActualizacionVinos = None

    def opImportarActualizacionVinos():
        listaBodegasParaActualizar = GestorImportarActualizaciones.buscarBodegasParaActualizar()
        return listaBodegasParaActualizar
    
    def buscarBodegasParaActualizar():
        listaBodegasParaActualizar = []
        bodegas = Bodega.objects.all()
        for bodega in bodegas:
            if bodega.estaParaActualizarVinos():
                nombre = bodega.getNombre()
                listaBodegasParaActualizar.append(nombre)
        return listaBodegasParaActualizar
    
    def tomarSeleccionBodega(id):
        bodegaSeleccionada = Bodega.objects.get(id = id).getNombre

        datosActualizacionVinos = GestorImportarActualizaciones.obtenerActualizacionVinosBodega(bodegaSeleccionada)
        return
    
    def obtenerActualizacionVinosBodega(bodega):
        actualizaciones = InterfazApiBodegas.obtenerActualizacionVinos(bodega)
        return actualizaciones

    def actualizarVinoExistente(self):
        return
    
    def buscarMaridaje(self):
        return
    
    def buscarTipoUva(self):
        return
    
    def crearVinos(self):
        return
    
    def buscarSeguidoresDeBodega(self):
        return
    
    def finCU(self):
        return
from django.shortcuts import render

from .interfaces import *
from .models import *
import json

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
    
    def tomarSeleccionBodega(nom):
        bodegaSeleccionada = Bodega.objects.get(nombre = nom).getNombre()
        actualizaciones = GestorImportarActualizaciones.obtenerActualizacionVinosBodega(bodegaSeleccionada)
        return actualizaciones
    
    def obtenerActualizacionVinosBodega(bodega):
        actualizaciones = InterfazApiBodegas.obtenerActualizacionVinos(bodega)
        
        with open(actualizaciones, encoding='utf-8') as file:
            data = json.load(file)
           
        return data

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
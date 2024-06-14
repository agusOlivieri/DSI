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
        return GestorImportarActualizaciones.actualizarOCrearVino(actualizaciones, bodegaSeleccionada)
        
    
    def obtenerActualizacionVinosBodega(bodega):
        actualizaciones = InterfazApiBodegas.obtenerActualizacionVinos(bodega)
        
        with open(actualizaciones, encoding='utf-8') as file:
            data = json.load(file)
           
        return data

    def actualizarOCrearVino(actualizaciones, bodegaSeleccionada):
        vinosImportados = []
        bod = Bodega.objects.get(nombre=bodegaSeleccionada)

        for actualizacion in actualizaciones:
            if Bodega.esVinoParaActualizar(actualizacion, bod): # <- por cada actualizacion valida si el vino existe, si es así, lo actualiza, si no, lo crea.
                Bodega.actualizarDatosVino(actualizacion)
                print("vino actualizado", actualizacion.get('nombre'))
            else: # <- creamos el vino
                # primero validamos que existan el maridaje y el tipo de uva en nuestra BD
                # if (GestorImportarActualizaciones.buscarMaridaje() and GestorImportarActualizaciones.buscarTipoUva()):
                print("to do")
            

            # print(Bodega.actualizarDatosVino(actualizacion, vinos))

        # vinosImportados = Vino.objects.filter(bodega=bodegaSeleccionada.id)
        # return vinosImportados

    
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
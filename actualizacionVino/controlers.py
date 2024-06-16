from django.shortcuts import render

from .interfaces import *
from .models import *
#from .views import PantallaImportarActualizaciones
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
        bodegaSeleccionada = Bodega.objects.get(nombre = nom)
        actualizaciones = GestorImportarActualizaciones.obtenerActualizacionVinosBodega(bodegaSeleccionada)

        return GestorImportarActualizaciones.actualizarOCrearVinos(actualizaciones, bodegaSeleccionada)
        
    
    def obtenerActualizacionVinosBodega(bodegaSeleccionada):
        nombreBodega = bodegaSeleccionada.nombre
        actualizaciones = InterfazApiBodegas.obtenerActualizacionVinos(nombreBodega)
        with open(actualizaciones, encoding='utf-8') as file:
            data = json.load(file)

        return data

    def actualizarOCrearVinos(actualizaciones, bod):
        vinosImportados = []

        for actualizacion in actualizaciones:

            vinoParaActualizar = bod.esVinoParaActualizar(actualizacion.get('nombre'))

            if vinoParaActualizar != None: # <- por cada actualizacion valida si el vino existe, lo actualiza, si no, lo crea.
                imagen = actualizacion.get('ImagenEtiqueta')
                notaDeCata = actualizacion.get('NotaDeCata')
                precio = actualizacion.get('precioARS')
                vino = bod.actualizarDatosVino(vinoParaActualizar, imagen, notaDeCata, precio)
                vinosImportados.append(vino)
                print("vino actualizado", actualizacion.get('nombre'))
            else: # <- creamos el vino
                # primero buscamos el maridaje y el tipo de uva en nuestra BD
                maridaje = GestorImportarActualizaciones.buscarMaridaje(actualizacion.get('maridaje'))
                tipoUva = GestorImportarActualizaciones.buscarTipoUva(actualizacion.get('varietal').get('tipoUva'))
                if (maridaje != None and tipoUva != None):
                    nom = actualizacion.get('nombre')
                    añada = actualizacion.get("añada")
                    imagen = actualizacion.get('ImagenEtiqueta')
                    notaDeCata = actualizacion.get('NotaDeCata')
                    precio = actualizacion.get('precioARS')

                    descVarietal = actualizacion.get('varietal').get('descripcion')
                    porcentajeComp = actualizacion.get('varietal').get('PorcentajeComposicion')

                    vino = bod.crearVino(nom, añada, imagen, notaDeCata, precio, maridaje, descVarietal, porcentajeComp, tipoUva)
                    vinosImportados.append(vino)
                    print("Vino creado")

        if vinosImportados != []:
            resumenVinosImportados = []
            for vino in vinosImportados:
                resumenVinosImportados.append({
                    'nombre':vino.nombre,
                    'añada':vino.añada,
                    'precio':vino.precioARS,
                    'imagenEtiqueta':vino.imagenEtiqueta
                })
            return resumenVinosImportados

#            PantallaImportarActualizaciones.mostrarResumenVinosImportados(resumenVinosImportados)

        
    
    def buscarMaridaje(mar):
        maridajes = Maridaje.objects.all()

        for maridaje in maridajes:
            if maridaje.esMaridaje(mar):
                return maridaje
        return None
    
    def buscarTipoUva(tipo):
        tiposUva = TipoUva.objects.all()

        for tipoUva in tiposUva:
            if tipoUva.esTipoUva(tipo):
                return tipoUva
        return None
    
    def buscarSeguidoresDeBodega(self):
        return
    
    def finCU(self):
        return
from models import *
import json



def inicializarMaridajes():
    with open("./inicializadores/InicializadorMaridajes.json") as file:
        data = json.load(file)

    for maridaje in data:
        nombre = maridaje.get('nombre')
        descripcion = maridaje.get('descripcion')

        nuevoMaridaje = Maridaje(nombre, descripcion)
        nuevoMaridaje.save()


def inicializarBodegas():
    with open("./inicializadores/InicializadorBodegas.json") as file:
        data = json.load(file)

    for bodega in data:
        nombre = bodega.get('nombre')
        descripcion = bodega.get('descripcion')
        historia = bodega.get('historia')
        periodoActualizacion = bodega.get('periodoActualizacion')
        ultimaActualizacion = bodega.get('ultimaActualizacion')

        nuevaBodega = Bodega(nombre, descripcion, historia, periodoActualizacion, ultimaActualizacion)
        nuevoBodega.save()

def inicializarVinos():
    with open("./inicializadores/InicializadorVino.json") as file:
        data = json.load(file)

    for vino in data:
        nombre = vino.get('nombre')
        añada = vino.get('añada')
        imagenEtiqueta = vino.get('ImagenEtiqueta')
        notaDeCata = vino.get('NotaDeCata')
        precioARS = vino.get('precioARS')
        bodega = Bodega.models.get(pk=vino.get('bodega'))
        maridaje = Maridaje.models.get(pk=vino.get('maridaje'))
        varietal = Varietal.new(vino['varietal']['descripcion'], vino['varietal']['PorcentajeComposicion'], vino['varietal']['tipoUva'])

        nuevoVino = Vino(nombre, añada, imagenEtiqueta, notaDeCata, precioARS, bodega, maridaje, varietal)
        nuevoVino.save()

inicializarMaridajes()
inicializarBodegas()
inicializarVinos()
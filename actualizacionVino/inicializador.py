from .models import *
import json

def inicializarMaridajes():
    with open("InicializadorMaridajes.json") as file:
        data = json.load(file)

    id = 1
    for maridaje in data:
        nombre = maridaje.get('nombre')
        descripcion = maridaje.get('descripcion')

        nuevoMaridaje = Maridaje(id, nombre, descripcion)
        nuevoMaridaje.save()
        id += 1


def inicializarBodegas():
    with open("InicializadorBodegas.json") as file:
        data = json.load(file)

    id = 1
    for bodega in data:
        nombre = bodega.get('nombre')
        descripcion = bodega.get('descripcion')
        historia = bodega.get('historia')
        periodoActualizacion = bodega.get('periodoActualizacion')
        ultimaActualizacion = bodega.get('ultimaActualizacion')

        nuevaBodega = Bodega(id, nombre, descripcion, historia, periodoActualizacion, ultimaActualizacion)
        nuevaBodega.save()
        id += 1

def inicializarVinos():
    with open("InicializadorVinos.json", encoding='utf-8') as file:
        data = json.load(file)

    id = 1
    for vino in data:
        añada = vino.get('añada')
        imagenEtiqueta = vino.get('ImagenEtiqueta')
        notaDeCata = vino.get('NotaDeCata')
        precioARS = vino.get('precioARS')
        bodega = Bodega.objects.get(pk=vino.get('bodega'))
        maridaje = Maridaje.objects.get(pk=vino.get('maridaje'))
        tipoUva = TipoUva.objects.get(nombre=vino['varietal']['tipoUva'])
        nombre = vino.get('nombre')
        print("--------")
        print(tipoUva.id)
        print("--------")
        
        varietal = Varietal(id, vino['varietal']['descripcion'], vino['varietal']['PorcentajeComposicion'], tipoUva.id)
        varietal.save()
        nuevoVino = Vino(id, nombre, añada, imagenEtiqueta, notaDeCata, precioARS, bodega.id, maridaje.id, varietal.id)
        nuevoVino.save()
        id += 1

def inicializarTipoUvas():
    with open("InicializadorTipoUva.json") as file:
        data = json.load(file)

    id = 1
    for tipo in data:
        nombre = tipo.get('nombre')
        descripcion = tipo.get('descripcion')
        nuevoTipoUva = TipoUva(id, nombre, descripcion)
        nuevoTipoUva.save()
        id += 1


def inicializar(request):
    # inicializarMaridajes()
    # inicializarTipoUvas()
    # inicializarBodegas()
    inicializarVinos()
    print("objetos creados")


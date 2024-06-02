from .models import *
from django.http import HttpResponse
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
        nom = vino.get('nombre')
        aniada = vino.get('añada')
        imagen = vino.get('ImagenEtiqueta')
        notaDeCata = vino.get('NotaDeCata')
        precio = vino.get('precioARS')

        bod = Bodega.objects.get(id=vino.get('bodega'))
        mar = Maridaje.objects.get(id=vino.get('maridaje'))
        tipouva = TipoUva.objects.get(id=vino['varietal']['tipoUva'])
        
        var = Varietal(descripcion=vino['varietal']['descripcion'], porcentajeComposicion=vino['varietal']['PorcentajeComposicion'], tipoUva=tipouva)
        var.save()

        nuevoVino = Vino(nombre=nom, añada=aniada, imagenEtiqueta=imagen, notaDeCataBodega=notaDeCata, precioARS=precio, maridaje=mar, varietal=var, bodega=bod)
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
    inicializarMaridajes()
    inicializarTipoUvas()
    inicializarBodegas()
    inicializarVinos()
    print("objetos creados")
    return HttpResponse("<h1>Objetos inicializados</h1>")


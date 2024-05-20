from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import json
# Create your views here.

def index(request): 
    return render(request, 'index.html')

def verActualizaciones(request):
    with open("actualizaciones.json") as file:
        data = json.load(file)
    return render(request, 'ver_actualizaciones.html', {
        'json': data
    })

def actualizarVino(request):
    r = RegionVitinicola.objects.get(id=1)
    b = Bodega(nombre="prueba", perActualizacion=13, region=r)
    b.save()
    bodegas = list(Bodega.objects.values())
    return JsonResponse(bodegas, safe=False)

def crearVino(request, id):
    with open("actualizaciones.json") as file:
        data = json.load(file)

    actualizaciones = data["bodegas"]
    listaVinos = []
    for a in actualizaciones:
        if a["id"] == id:

            maridajeId = a["vino"]["maridaje"]
            varietalId = a["vino"]["varietal"]
            m = Maridaje.objects.get(id=maridajeId)
            v = Varietal.objects.get(id=varietalId)
            b = Bodega.objects.get(id=id)
            
            aniada = a["vino"]["aniada"]
            imagen = a["vino"]["ImagenEtiqueta"]
            nota = a["vino"]["NotaDeCata"]
            precio = a["vino"]["precioARS"]
            nom = a["vino"]["nombre"]

            vino = Vino(añada=aniada, ImagenEstiqueta=imagen, nombre=nom, notaDeCata=nota, precioARS=precio, maridaje=m, varietal=v, bodega=b)
            listaVinos.append(vino)
            vino.save()

    bodega = Bodega.objects.get(id=id)
    return render(request, 'lista_de_vinos.html', {
        "vinos": listaVinos,
        "bodega": bodega
    })
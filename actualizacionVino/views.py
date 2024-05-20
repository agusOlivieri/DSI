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



def actualizarVino(request, id):
    with open("actualizaciones.json") as file:
        data = json.load(file)
    
    actualizaciones = data["bodegas"][id-1]["actualizaciones"]

    listaVinos = []

    for a in actualizaciones:
        if (a["crear"] == False):
            vinoId = a["id"]
            precio = a["precioARS"]
            nota = a["NotaDeCata"]
            imagen = a["ImagenEtiqueta"]

            vino = Vino.objects.get(id=vinoId)
            vino.precioARS = precio
            vino.notaDeCata = nota
            vino.ImagenEstiqueta = imagen
            vino.save()
            listaVinos.append(vino)

        elif (a["crear"] == True):
            maridajeId = a["maridaje"]
            varietalId = a["varietal"]
            m = Maridaje.objects.get(id=maridajeId)
            v = Varietal.objects.get(id=varietalId)
            b = Bodega.objects.get(id=id)
            
            aniada = a["aniada"]
            imagen = a["ImagenEtiqueta"]
            nota = a["NotaDeCata"]
            precio = a["precioARS"]
            nom = a["nombre"]

            vino = Vino(añada=aniada, ImagenEstiqueta=imagen, nombre=nom, notaDeCata=nota, precioARS=precio, maridaje=m, varietal=v, bodega=b)
            vino.save()
            listaVinos.append(vino)

    bodega = Bodega.objects.get(id=id)
    return render(request, 'lista_de_vinos.html', {
        "vinos": listaVinos,
        "bodega": bodega
    })

# def crearVino(request, id):
#     with open("actualizaciones.json") as file:
#         data = json.load(file)

#     actualizaciones = data["bodegas"]
#     listaVinos = []
#     for a in actualizaciones:
#         if (a["id"] == id and a["crear"] == True):

#             maridajeId = a["vino"]["maridaje"]
#             varietalId = a["vino"]["varietal"]
#             m = Maridaje.objects.get(id=maridajeId)
#             v = Varietal.objects.get(id=varietalId)
#             b = Bodega.objects.get(id=id)
            
#             aniada = a["vino"]["aniada"]
#             imagen = a["vino"]["ImagenEtiqueta"]
#             nota = a["vino"]["NotaDeCata"]
#             precio = a["vino"]["precioARS"]
#             nom = a["vino"]["nombre"]

#             vino = Vino(añada=aniada, ImagenEstiqueta=imagen, nombre=nom, notaDeCata=nota, precioARS=precio, maridaje=m, varietal=v, bodega=b)
#             vino.save()
#             listaVinos.append(vino)

#     bodega = Bodega.objects.get(id=id)
#     return render(request, 'lista_de_vinos.html', {
#         "vinos": listaVinos,
#         "bodega": bodega
#     })
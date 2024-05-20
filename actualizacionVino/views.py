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
    print(data["bodegas"][0]["id"])
    return render(request, 'ver_actualizaciones.html', {
        'json': data
    })

def actualizarVino(request):
    r = RegionVitinicola.objects.get(id=1)
    b = Bodega(nombre="prueba", perActualizacion=13, region=r)
    b.save()
    bodegas = list(Bodega.objects.values())
    return JsonResponse(bodegas, safe=False)

def crearVino(request):
    with open("actualizaciones.json") as file:
        data = json.load(file)
    #v = Maridaje.objects.get(id=data.bodega.vino.)
    return HttpResponse('pruebas')
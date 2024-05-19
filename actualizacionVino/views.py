from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import json
# Create your views here.

def index(request): 
    return render(request, 'index.html')

def vinos(request):
    vinos = list(Vino.objects.values())
    return JsonResponse(vinos, safe=False)

def verJson(request):
    with open("actualizaciones.json") as file:
        data = json.load(file)
    print(data)
    return JsonResponse(data)

def actualizar_vinos(request):
    r = RegionVitinicola.objects.get(id=1)
    b = Bodega(nombre="prueba", perActualizacion=13, region=r)
    b.save()
    bodegas = list(Bodega.objects.values())
    return JsonResponse(bodegas, safe=False)
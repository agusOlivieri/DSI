from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *

# Create your views here.

def hello(request): 
    return HttpResponse("<h1>Hello World</h1>")

def vinos(request):
    vinos = list(Vino.objects.values())
    return JsonResponse(vinos, safe=False)
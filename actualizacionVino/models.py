from django.db import models

# Create your models here.

class RegionVitinicola(models.Model):
    descrip = models.TextField()
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    descrip = models.TextField()
    historia = models.CharField(max_length=50)
    perActualizacion = models.IntegerField()
    coordenadasUbi = models.CharField(max_length=50)
    region = models.ForeignKey(RegionVitinicola, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Maridaje(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Varietal(models.Model):
    nombre = models.CharField(max_length=30)
    descrip = models.TextField()
    porcComposicion = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Vino(models.Model):
    añada = models.CharField(max_length=100)
    ImagenEstiqueta = models.CharField(max_length=200)
    nombre = models.CharField(max_length=50)
    notaDeCata = models.CharField(max_length=100)
    precioARS = models.IntegerField()
    maridaje = models.ForeignKey(Maridaje, on_delete=models.CASCADE)
    varietal = models.ForeignKey(Varietal, on_delete=models.CASCADE)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre









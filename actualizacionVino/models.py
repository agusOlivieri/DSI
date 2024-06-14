from django.db import models
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta

# Create your models here.

class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    historia = models.TextField()
    periodoActualizacion = models.IntegerField()
    ultimaActualizacion = models.DateTimeField()
    
    def getNombre(self):
        return self.nombre
    
    def estaParaActualizarVinos(self):
        now_aware = datetime.now(timezone.utc)
        if not self.ultimaActualizacion:
            # Si nunca se ha actualizado, se puede actualizar de inmediato
            return True

        # Calcular la próxima fecha de actualización sumando los meses del periodo de actualizacion a la ultima actualizacion (usamos relativedelta para ser mas precisos)
        proximaActualizacion = self.ultimaActualizacion + relativedelta(months=self.periodoActualizacion)
        
        # Comparar la próxima fecha de actualización con la fecha actual, si la fecha actual es mayor o igual a la proxima actualizacion retorna true
        return now_aware >= proximaActualizacion
    
    def esVinoParaActualizar(actualizacion, bod):
        nom = actualizacion.get('nombre')
        
        if (list(Vino.objects.filter(nombre=nom).filter(bodega=bod)) != []):
            print(Vino.objects.filter(nombre=nom, bodega=bod))
            return True
        return False

    def actualizarDatosVino(actualizacion):
        nom = actualizacion.get('nombre')
        imagen = actualizacion.get('ImagenEtiqueta')
        notaDeCata = actualizacion.get('NotaDeCata')
        precio = actualizacion.get('precioARS')

        vino = Vino.objects.get(nombre=nom)

        vino.setPrecio(precio)
        vino.setNotaCata(notaDeCata)
        vino.setImagenEtiqueta(imagen)
        vino.save() # Guardamos el vino actualizado

    def crearVino(actualizacion):
        nom = actualizacion.get('nombre')
        añada = actualizacion.get("añada")
        imagen = actualizacion.get('ImagenEtiqueta')
        notaDeCata = actualizacion.get('NotaDeCata')
        precio = actualizacion.get('precioARS')
        bod = actualizacion.get('bodega')
        mar = actualizacion.get('maridaje')

        descVarietal = actualizacion.get('varietal').get('descripcion')
        porcentajeComp = actualizacion.get('varietal').get('PorcentajeComposicion')
        tipoUva = actualizacion.get('varietal').get('tipoUva')
        
        Vino.newVino(añada, imagen, nom, precio, notaDeCata, mar, bod, descVarietal, porcentajeComp, tipoUva)

class TipoUva(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def esTipoUva(self, tipoId):
        return self.id == tipoId

class Maridaje(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def esMaridaje(self, marId):
        return self.id == marId

class Varietal(models.Model):
    descripcion = models.TextField()
    porcentajeComposicion = models.IntegerField()
    tipoUva = models.ForeignKey(TipoUva, on_delete=models.CASCADE)

    def newVarietal(desc, porcentaje, tipo):
        print(desc)
        varietal = Varietal(descripcion=desc, porcentajeComposicion=porcentaje, tipoUva=tipo)
        varietal.save()
        return varietal
    
class Vino(models.Model):
    nombre = models.CharField(max_length=50)
    añada = models.IntegerField()
    imagenEtiqueta = models.CharField(max_length=200)
    notaDeCataBodega = models.CharField(max_length=300)
    precioARS = models.IntegerField()
    maridaje = models.ForeignKey(Maridaje, on_delete=models.CASCADE)
    varietal = models.ForeignKey(Varietal, on_delete=models.CASCADE)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
   
    class Meta:
        unique_together = ('nombre', 'añada')  # Definir una restricción de unicidad para el nombre y la añada (pk)

    def newVino(aña, imagen, nom, precio,notaDeCata, maridajeId, bodegaId, descVarietal, porcentajeComp, tipoUva):
        tu = TipoUva.objects.get(id=tipoUva) #<- tipo uva 
        
        nuevoVarietal = Vino.crearVarietal(descVarietal, porcentajeComp, tu)
        bod = Bodega.objects.get(id=bodegaId)
        mar = Maridaje.objects.get(id=maridajeId)

        vino = Vino(nombre=nom, añada=aña, imagenEtiqueta=imagen, notaDeCataBodega=notaDeCata, precioARS=precio, maridaje=mar, varietal=nuevoVarietal, bodega=bod)
        vino.save()     
 
    def esVinoParaActualizar(nom, vino):
        print(vino.nombre)
        if vino.nombre == nom:
            return True
        return False
    
    def setPrecio(self, precio):
        self.precioARS = precio
        self.save()
    
    def setNotaCata(self, nota):
        self.notaDeCataBodega = nota
        self.save()
    
    def setImagenEtiqueta(self, imagen):
        self.imagen = imagen
        self.save()
    
    def crearVarietal(descVarietal, porcentajeComp, tipoUva):
        return Varietal.newVarietal(descVarietal, porcentajeComp, tipoUva)
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    premium = models.BooleanField()
    password = models.CharField(max_length=30)

    def getNombre(self):
        return self.nombre
     
class Siguiendo(models.Model):
    fechaFin = models.DateField()
    fechaInicio = models.DateField()
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)

    def sosDeBodega(self, nombreBodega):
        return (self.bodega.nombre == nombreBodega)

class Enofilo(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    imagenPerfil = models.CharField(max_length=30)
    siguiendo = models.ForeignKey(Siguiendo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vino = models.ForeignKey(Vino, on_delete=models.CASCADE)

    def getNombreUsuario(self):
        return self.usuario.getNombre()

    def seguisABodega(self, nombreBodega):
        return self.siguiendo.sosDeBodega(nombreBodega)
    


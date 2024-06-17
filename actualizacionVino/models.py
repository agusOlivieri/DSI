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
    
    def esVinoParaActualizar(self, nom):
        vinos_de_bodega = self.vinos.all() # accedemos a los vinos asociados a esta bodega usando el related_name 'vinos'
        for vino in vinos_de_bodega:
            if vino.esVinoParaActualizar(nom):
                return vino
            else:
                continue
        return None

    def actualizarUltimaFecha(self):
        self.ultimaActualizacion = datetime.now(timezone.utc)
        self.save()

    def actualizarDatosVino(self, vino, imagen, notaDeCata, precio):
        vino.setPrecio(precio)
        vino.setNotaCata(notaDeCata)
        vino.setImagenEtiqueta(imagen)
        vino.save()
        return vino

    def crearVino(self, nom, añada, imagen, notaDeCata, precio, maridaje, descVarietal, porcentajeComp, tipoUva):
        return Vino.newVino(añada, imagen, nom, precio, notaDeCata, maridaje, self, descVarietal, porcentajeComp, tipoUva)

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
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, related_name='vinos') #related_name usado para acceder a los vinos relacionados a una bodega
   
    class Meta:
        unique_together = ('nombre', 'añada')  # Definir una restricción de unicidad para el nombre y la añada (pk)

    def newVino(aña, imagen, nom, precio,notaDeCata, maridaje, bodega, descVarietal, porcentajeComp, tipoUva):
        
        nuevoVarietal = Vino.crearVarietal(descVarietal, porcentajeComp, tipoUva)

        vino = Vino(nombre=nom, añada=aña, imagenEtiqueta=imagen, notaDeCataBodega=notaDeCata, precioARS=precio, maridaje=maridaje, varietal=nuevoVarietal, bodega=bodega)
        vino.save()
        return vino  
 
    def esVinoParaActualizar(self, nom):
        return self.nombre == nom
    
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

    def sosDeBodega(self, bod):
        return (self.bodega.id == bod)

class Enofilo(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    imagenPerfil = models.CharField(max_length=30)
    siguiendo = models.ForeignKey(Siguiendo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vino = models.ForeignKey(Vino, on_delete=models.CASCADE)

    def getNombreUsuario(self):
        return self.usuario.getNombre()

    def seguisABodega(self, bodega):
        return self.siguiendo.sosDeBodega(bodega)
    


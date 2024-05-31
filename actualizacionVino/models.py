from django.db import models
from django.db.models import Q

# Create your models here.

class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    historia = models.CharField(max_length=50)
    periodoActualizacion = models.IntegerField()
    coordenadasUbicacion = models.CharField(max_length=50)

    def getNombre(self):
        return self.nombre
    
    def estaParaActualizarVinos(self):
        return
    
    def actualizarDatosVino(self):
        return

class TipoUva(models.Model):
    descripcion = models.TextField()
    nombre = models.CharField(max_length=50)

    def esTipoUva(self):
        return 

class Maridaje(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def esMaridaje(self):
        return

class Varietal(models.Model):
    descripcion = models.TextField()
    porcentajeComposicion = models.FloatField()
    tipoUva = models.ForeignKey(TipoUva, on_delete=models.CASCADE)

    #Agregar a diagrama de clases
    def esTipoUva(self, uva):

        if uva == self.tipoUva:
            return True 
                  #(TipoUva.objects.get(pk=uva))
        return False

    def new(self, descripcion, porcentajeComposicion, tipoUva):
        varietal = Varietal
        varietal.descripcion = descripcion
        varietal.porcentajeComposicion = porcentajeComposicion
        varietal.tipoUva = tipoUva
        varietal.save()
        return 
    
    
class Vino(models.Model):
    añada = models.CharField(max_length=100)
    imagenEtiqueta = models.CharField(max_length=200)
    nombre = models.CharField(max_length=50)
    notaDeCataBodega = models.CharField(max_length=100)
    precioARS = models.IntegerField()
    maridaje = models.ForeignKey(Maridaje, on_delete=models.CASCADE)
    varietal = models.ForeignKey(Varietal, on_delete=models.CASCADE)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
   
    def newVino(añada, imagenEtiqueta, nombre, precioARS,notaDeCataBodega, idmaridaje, bodega, nombreVarietal, descVarietal, porcentajeComp, tipoUva):
        varietal = Varietal.new(nombreVarietal, descVarietal, porcentajeComp, tipoUva)
        maridaje = Maridaje.objects.get(pk=idmaridaje)

        vino = Vino
        vino.añada = añada
        vino.imagenEtiqueta = imagenEtiqueta
        vino.nombre = nombre
        vino.precioARS = precioARS
        vino.notaDeCataBodega = notaDeCataBodega
        vino.maridaje = maridaje
        vino.varietal = varietal.id
        vino.bodega = bodega

        vino.save()
        varietal.save()       


       
        
    def esVinoParaActualizar(self, añada, nombre):
        if (self.añada == añada and self.nombre == nombre):
            return self
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
    
    def crearVarietal(self, nombreVarietal, descVarietal, porcentajeComp, tipoUva):
        Varietal.new(nombreVarietal, descVarietal, porcentajeComp, tipoUva)
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    premium = models.BooleanField()
    password = models.CharField()

    def getNombre(self):
        return self.nombre
    

class Siguiendo(models.Model):
    fechaFin = models.DateField()
    fechaInicio = models.DateField()
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)

    def sosDeBodega(self):
        return

class Enofilo(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    imagenPerfil = models.ImageField()
    siguiendo = models.ForeignKey(Siguiendo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vino = models.ForeignKey(Vino, on_delete=models.CASCADE)

    def getNombreUsuario(self):
        return
    
    def seguisABodega(self):
        return
    
class InterfazApiBodega(models.Model):
    

    def obtenerActualizacionVinos(self):
        return

class InterfazNotificacionPush(models.Model):
    
    def notificarEnofilo(enofilo):
        notificado = True
        #no implementado
        return notificado

    def notificarNovedadVinoParaBodega(self, enofilos):

        for i in range(len(enofilos)):
            self.notificarEnofilo(enofilos[i].usuario)

        return ('Enofilos notificados con éxito.')

class PantallaImportarActualizaciones(models.Model):
    listaBodegasParaActualizar = []
    resumenVinosImportados = []
    seleccionBodega = None

    def opImportarActualizacionVinos(self):
        return
    
    def habilitar(self):
        return

    def mostrarBodegasParaActualizar(self):
        return
    
    def tomarSeleccionBodega(self):
        return

    def mostrarResumenVinosImportados(self):
        return

class GestorImportarActualizaciones(models.Model):
    seleccionBodega = None
    listaBodegasParaActualizar = []
    tipoUva = None
    maridaje = None
    listaSeguidoresDeBodega = []
    datosActualizacionVinos = None

    def opImportarActualizacionVinos(self):
        return
    
    def buscarBodegasParaActualizar(self):
        return

    def tomarSeleccionBodega(self):
        return
    
    def obtenerActualizacionVinosBodega(self):
        return

    def actualizarVinoExistente(self):
        return
    
    def buscarMaridaje(self):
        return
    
    def buscarTipoUva(self):
        return
    
    def crearVinos(self):
        return
    
    def buscarSeguidoresDeBodega(self):
        return
    
    def finCU(self):
        return
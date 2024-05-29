from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create your models here.

class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    historia = models.CharField(max_length=50)
    periodoActualizacion = models.IntegerField()
    coordenadasUbicacion = models.CharField(max_length=50)
    ultimaActualizacion = models.DateTimeField()

    def getNombre(self):
        return self.nombre
    
    def estaParaActualizarVinos(self):
        if not self.ultimaActualizacion:
            # Si nunca se ha actualizado, se puede actualizar de inmediato
            return True

        # Calcular la próxima fecha de actualización sumando los meses del periodo de actualizacion a la ultima actualizacion (usamos relativedelta para ser mas precisos)
        proximaActualizacion = self.ultimaActualizacion + relativedelta(months=self.periodoActualizacion)
        
        # Comparar la próxima fecha de actualización con la fecha actual, si la fecha actual es mayor o igual a la proxima actualizacion retorna true
        return datetime.now() >= proximaActualizacion
    
    def actualizarDatosVino(self, nombre, añada, precio=None, nota_de_cata=None, imagen_etiqueta=None):
        vinos = self.vino_set.all()  # Obtener todos los vinos que apuntan a esta bodega para buscar el que tenemos
        for vino in vinos:
            if vino.esVinoParaActualizar(nombre, añada):
                if precio is not None:
                    vino.setPrecio(precio)
                if nota_de_cata is not None:
                    vino.setNotaCata(nota_de_cata)
                if imagen_etiqueta is not None:
                    vino.setImagenEtiqueta(imagen_etiqueta)
                vino.save() # Guardamos el vino actualizado
                return True
            else: 
                return False # No se encontro el vino para actualizar
        

class TipoUva(models.Model):
    descripcion = models.TextField()
    nombre = models.CharField(max_length=50)

    def esTipoUva(self, nombre):
        return self.nombre == nombre

class Maridaje(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def esMaridaje(self, nombre):
        return self.nombre == nombre

class Varietal(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    porcentajeComposicion = models.FloatField()
    tipoUva = models.ForeignKey(TipoUva, on_delete=models.CASCADE)

    def new(self):
        return
    
class Vino(models.Model):
    añada = models.CharField(max_length=100)
    ImagenEtiqueta = models.CharField(max_length=200)
    nombre = models.CharField(max_length=50)
    notaDeCataBodega = models.CharField(max_length=100)
    precioARS = models.IntegerField()
    maridaje = models.ForeignKey(Maridaje, on_delete=models.CASCADE)
    varietal = models.ForeignKey(Varietal, on_delete=models.CASCADE)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('nombre', 'añada')  # Definir una restricción de unicidad para el nombre y la añada (pk)
   
    def esVinoParaActualizar(self, nombre, añada): # con el nombre y la añada podemos identificar cualquier vino
        return (self.añada == añada and self.nombre == nombre)
    
    def setPrecio(self, precio):
        self.precioARS = precio
    
    def setNotaCata(self):
        return
    
    def setImagenEtiqueta(self):
        return
    
    def crearVarietal(self):
        return
    
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

    def sosDeBodega(self):
        return

class Enofilo(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    imagenPerfil = models.Field()
    siguiendo = models.ForeignKey(Siguiendo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vino = models.ForeignKey(Vino, on_delete=models.CASCADE)

    def getNombreUsuario(self):
        return self.usuario.nombre
    
    def seguisABodega(self):
        return
    
class InterfazApiBodega(models.Model):
    

    def obtenerActualizacionVinos(self):
        return

class InterfazNotificacionPush(models.Model):
    

    def notificarNovedadVinoParaBodega(self):
        return

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
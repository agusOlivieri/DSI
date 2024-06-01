from django.db import models
from datetime import datetime
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
        if not self.ultimaActualizacion:
            # Si nunca se ha actualizado, se puede actualizar de inmediato
            return True

        # Calcular la próxima fecha de actualización sumando los meses del periodo de actualizacion a la ultima actualizacion (usamos relativedelta para ser mas precisos)
        proximaActualizacion = self.ultimaActualizacion + relativedelta(months=self.periodoActualizacion)
        
        # Comparar la próxima fecha de actualización con la fecha actual, si la fecha actual es mayor o igual a la proxima actualizacion retorna true
        return datetime.now() >= proximaActualizacion
    
    def actualizarDatosVino(self, nombre, añada, precio, nota_de_cata, imagen_etiqueta):
        vinos = Vino.objects.all()  # Obtener todos los vinos que apuntan a esta bodega para buscar el que tenemos
        for vino in vinos:
            if vino.esVinoParaActualizar(nombre, añada) and (vino.bodega == self.id):
                vino.setPrecio(precio)
                vino.setNotaCata(nota_de_cata)
                vino.setImagenEtiqueta(imagen_etiqueta)
                vino.save() # Guardamos el vino actualizado
                return True
            else: 
                return False # No se encontro el vino para actualizar
        

class TipoUva(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def esTipoUva(self, nombre):
        return self.nombre == nombre

class Maridaje(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def esMaridaje(self, nombre):
        return self.nombre == nombre

class Varietal(models.Model):
    descripcion = models.TextField()
    porcentajeComposicion = models.IntegerField()
    tipoUva = models.ForeignKey(TipoUva, on_delete=models.CASCADE)

    def new(descripcion, porcentajeComposicion, tipoUva):
        varietal = Varietal
        varietal.descripcion = descripcion
        varietal.porcentajeComposicion = porcentajeComposicion
        varietal.tipoUva = tipoUva
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

    def newVino(self, añada, imagenEtiqueta, nombre, precioARS,notaDeCataBodega, nombreMaridaje, bodega, nombreVarietal, descVarietal, porcentajeComp, tipoUva):
        varietal = self.crearVarietal(nombreVarietal, descVarietal, porcentajeComp, tipoUva)
        maridaje = Maridaje.objects.get(nombre=nombreMaridaje)

        vino = Vino
        vino.añada = añada
        vino.imagenEtiqueta = imagenEtiqueta
        vino.nombre = nombre
        vino.precioARS = precioARS
        vino.notaDeCataBodega = notaDeCataBodega
        vino.maridaje = maridaje
        vino.varietal = varietal
        vino.bodega = bodega

        vino.save()     

        
    def esVinoParaActualizar(self, añada, nombre):
        if (self.añada == añada and self.nombre == nombre):
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
    
    def crearVarietal(self, nombreVarietal, descVarietal, porcentajeComp, tipoUva):
        return Varietal.new(nombreVarietal, descVarietal, porcentajeComp, tipoUva)
    
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
    


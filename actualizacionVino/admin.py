from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Vino)
admin.site.register(Bodega)
admin.site.register(Maridaje)
admin.site.register(Varietal)
admin.site.register(TipoUva)
admin.site.register(Usuario)
admin.site.register(Siguiendo)
admin.site.register(Enofilo)
admin.site.register(InterfazApiBodega)
admin.site.register(InterfazNotificacionPush)
admin.site.register(GestorImportarActualizaciones)
admin.site.register(PantallaImportarActualizaciones)

from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Vino)
admin.site.register(Bodega)
admin.site.register(Maridaje)
admin.site.register(Varietal)
admin.site.register(RegionVitinicola)
admin.site.register(TipoUva)
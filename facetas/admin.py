from django.contrib import admin
from .models import NivelOperacional, CargoGestores, Orgao, GestaoPrincial, UnidadeAdministrativa
# Register your models here.

admin.site.register(NivelOperacional)
admin.site.register(CargoGestores)
admin.site.register(Orgao)
admin.site.register(GestaoPrincial)
admin.site.register(UnidadeAdministrativa)

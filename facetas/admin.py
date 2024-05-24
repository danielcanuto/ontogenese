from django.contrib import admin
from .models import NivelOperacional, CargoGestores, Orgao, GestaoPrincial, UnidadeAdministrativa, GestorEstruturaPrincipal, Paises, Estado, Municipio
# Register your models here.

admin.site.register(NivelOperacional)
admin.site.register(Paises)
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(GestorEstruturaPrincipal)
admin.site.register(CargoGestores)
admin.site.register(Orgao)
admin.site.register(GestaoPrincial)
admin.site.register(UnidadeAdministrativa)

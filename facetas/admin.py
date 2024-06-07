from django.contrib import admin
from .models import OrgaoAtual, CargoGestao,TabelaGestor, GestorMaior, PeriodoHistorico
from .models import TipoAdminstracao, OrgaoUnidade, PeriodoHistoricoParte
from .models import NivelAdmin, Setor
from .models import ConfiguracaoFuncional
from .models import PrazoDeGuarda,GuardaCorrente,GuardaIntermediario, ClasseTTDD
from .models import Especie, TermoRemissivo, NormaEspecie, NormaTipologia, TipologiaDocumental

admin.site.register(OrgaoAtual)
admin.site.register(CargoGestao)
admin.site.register(TabelaGestor)
admin.site.register(GestorMaior)
admin.site.register(PeriodoHistorico)
admin.site.register(TipoAdminstracao)
admin.site.register(OrgaoUnidade)
admin.site.register(PeriodoHistoricoParte)
admin.site.register(NivelAdmin)
admin.site.register(Setor)
admin.site.register(ConfiguracaoFuncional)
admin.site.register(PrazoDeGuarda)
admin.site.register(GuardaCorrente)
admin.site.register(GuardaIntermediario)
admin.site.register(ClasseTTDD)
admin.site.register(Especie)
admin.site.register(TermoRemissivo)
admin.site.register(NormaEspecie)
admin.site.register(NormaTipologia)
admin.site.register(TipologiaDocumental)

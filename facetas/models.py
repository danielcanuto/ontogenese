from django.db import models

# Create your models here.
class NivelOperacional(models.Model):
    termo = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self):
        return self.termo


class CargoGestores(models.Model):
    nome_cargo = models.CharField(max_length=50)
    nivel_operacional = models.ForeignKey(
        NivelOperacional, on_delete=models.CASCADE, blank=True, null=True)
    observacao = models.TextField()
    def __str__(self):
        return self.nome_cargo



class Orgao(models.Model):
    nome_orgao = models.CharField(max_length=100)
    sigla_orgao = models.CharField(max_length=10)
    orgao_superior = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    inicio_atividades = models.DateField()
    termino_atividades = models.DateField()
    cargo_gestor = models.ForeignKey(CargoGestores, on_delete=models.CASCADE, blank=True, null=True)
    fundamentacao_legal = models.TextField()
    upload_fundamentacao = models.FileField(upload_to='fundamentacao/')
    observacao = models.TextField()

    def __str__(self):
        return self.nome_orgao


class GestaoPrincial(models.Model):
    nome_orgao_principal = models.CharField(max_length=100)
    sigla_orgao = models.CharField(max_length=10)
    cargo_gestor = models.ForeignKey(CargoGestores, on_delete=models.CASCADE, blank=True, null=True)
    inicio_atividades = models.DateField()
    termino_atividades = models.DateField()
    periodo_historico = models.CharField(max_length=100)
    fundamentacao_legal = models.TextField()
    upload_fundamentacao = models.FileField(upload_to='fundamentacao/')
    dados_biograficos = models.TextField()
    observacao = models.TextField()

    def __str__(self):
        return self.nome_orgao
    
class UnidadeAdministrativa(models.Model):
    orgao = models.ForeignKey(Orgao, on_delete=models.CASCADE, blank=True, null=True)
    nome_unidade = models.CharField(max_length=100)
    sigla_unidade = models.CharField(max_length=10)
    unidade_superior = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    cargo_gestor = models.ForeignKey(CargoGestores, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.nome_unidade} - {self.sigla_unidade}'
    
    
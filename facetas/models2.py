# from django.db import models
# from datetime import date

# # Create your models here.
# class NivelOperacional(models.Model):
#     termo = models.CharField(max_length=30)
#     descricao = models.TextField()

#     def __str__(self):
#         return self.termo

# class CargoGestao(models.Model):
#     nome_cargo = models.CharField(max_length=50)
#     nivel_operacional = models.ForeignKey(
#         NivelOperacional, on_delete=models.CASCADE, blank=True, null=True)
#     observacao = models.TextField()
    
#     def __str__(self):
#         return self.nome_cargo
    
# class Pais (models.Model):
#     nome_do_pais = models.CharField(max_length=50, default='Brasil')
#     sigla = models.CharField(max_length=2, default="BR")
#     observacao = models.TextField() 

#     def __str__(self):
#         return self.nome_do_pais

# class Estado (models.Model):
#     nacionalidade = models.ForeignKey(Pais, on_delete=models.CASCADE, blank=True, null=True)
#     nome_estado = models.CharField(max_length=50)
#     sigla_estado = models.CharField(max_length=2)
#     observacao = models.TextField()

#     def __str__(self):
#         return self.nome_estado

# class Municipio(models.Model):
#     estado = models.ForeignKey(Estado, on_delete=models.CASCADE, blank=True, null=True)
#     nome_municipio = models.CharField(max_length=50)
#     observacao = models.TextField()
    
#     def __str__(self):
#         return f'{self.nome_municipio} - {self.estado} -{self.estado.nacionalidade}'



# # Essa classe devera cadastrar o gestor do Período 
# class GestorEstruturaPrincipal(models.Model):
#     nome = models.CharField(max_length=50)
#     nascimento = models.DateField(default=date.today)
#     naturalidade = models.ForeignKey(Municipio, on_delete=models.CASCADE, blank=True, null=True)
#     observacao = models.TextField()

#     def __str__(self):
#         return self.nome

# #A Classe representa o momento historico do organização 
# # história do todo, o elo perdido

# class Orgao(models.Model): 
#     nome_orgao = models.CharField(max_length=100) # incluir nome do campo denominação do período histórico
#     sigla_orgao = models.CharField(max_length=10)
#     orgao_superior = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True) 
#     inicio_atividades = models.DateField()
#     termino_atividades = models.DateField()
#     gestor = models.ForeignKey(GestorEstruturaPrincipal, on_delete=models.CASCADE, blank=True, null=True)
#     cargo_gestor = models.ForeignKey(CargoGestao, on_delete=models.CASCADE, blank=True, null=True)
#     fundamentacao_legal = models.TextField()
#     upload_fundamentacao = models.FileField(upload_to='fundamentacao/')
#     observacao = models.TextField()

#     def __str__(self):
#         return self.nome_orgao

# # A classe representa o momento historico da organização
# class GestaoPrincial(models.Model):
#     nome_orgao_principal = models.CharField(max_length=100)
#     sigla_orgao = models.CharField(max_length=10)
#     cargo_gestor = models.ForeignKey(CargoGestao, on_delete=models.CASCADE, blank=True, null=True)
#     inicio_atividades = models.DateField()
#     termino_atividades = models.DateField()
#     periodo_historico = models.CharField(max_length=100)
#     fundamentacao_legal = models.TextField()
#     upload_fundamentacao = models.FileField(upload_to='fundamentacao/')
#     dados_biograficos = models.TextField()
#     observacao = models.TextField()

#     def __str__(self):
#         return self.nome_orgao_principal
    

# class UnidadeAdministrativa(models.Model):
#     orgao = models.ForeignKey(Orgao, on_delete=models.CASCADE, blank=True, null=True)
#     nome_unidade = models.CharField(max_length=100)
#     sigla_unidade = models.CharField(max_length=10)
#     unidade_superior = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
#     cargo_gestor = models.ForeignKey(CargoGestao, on_delete=models.CASCADE, blank=True, null=True)

#     def __str__(self):
#         return f'{self.nome_unidade} - {self.sigla_unidade}'
    

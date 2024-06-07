from django.db import models

# Escopo atual do todo(Fundo)
class OrgaoAtual(models.Model):
    # essas informações podem vim da tabela de registro do orgao
    # responsavel pela historico da instituição
    orgao_atual = models.CharField("Órgão Atual",max_length=150)
    sigla = models.CharField(max_length=50)

    inicio_atividades = models.DateField()
    fim_atividades = models.DateField(null=True, blank=True)

    orgao_antecessor = models.ForeignKey("self", 
                                         on_delete=models.CASCADE, blank=True, null=True, verbose_name="Órgão antecessor")

    def __str__(self):
        return f'{self.orgao_atual} - {self.sigla}'
    
    class Meta:
        verbose_name_plural = "Organizações do Todo"

# dados sobre o gestor

class CargoGestao(models.Model):
    nome_cargo = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome_cargo}'

class TabelaGestor(models.Model):
    nome = models.CharField(max_length=250)
    data_nascimento = models.DateField()
    data_obito = models.DateField(blank=True, null=True)
    
# Podem ser inseitos outros dados ou importados da tabela de cadastro funcional
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nome}'

class GestorMaior(models.Model):
    cargo_gestao = models.ForeignKey(
        CargoGestao, on_delete=models.CASCADE,blank=True, null=True, verbose_name="Cargo de Gestão"
    )
    nome_gestor = models.ForeignKey(
        TabelaGestor, on_delete=models.CASCADE, 
        blank=True, null=True, verbose_name="Nome do Gestor")
    data_nascimento = models.DateField()
    data_obito = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.cargo_gestao} - {self.nome_gestor}'

# dados sobre o perido historico da organização

class PeriodoHistorico(models.Model):
    denominacao = models.CharField(max_length=250, verbose_name="Denominação do Perído Histórico")
    organizacao = models.ForeignKey(
        OrgaoAtual, on_delete=models.CASCADE, blank=True, null=True,
        verbose_name="Orgão do Período")
    gestor_periodo = models.ForeignKey(
        GestorMaior, on_delete=models.CASCADE,blank=True, null=True, verbose_name="Gestor")
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    resumo = models.TextField(blank=True, null=True)
    doc_fundamento = models.FileField(upload_to='fundamentacao/', blank=True, null=True)
    obs = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.organizacao} - {self.denominacao}'
    class Meta:
        verbose_name_plural = "01 - Faceta História do Todo"

# Faceta Vinculo interinstitucional

class TipoAdminstracao(models.Model):
    denominação = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.denominação}'
    class Meta:
        verbose_name_plural = "Tipos de Administração"
class OrgaoUnidade(models.Model):
    periodo = models.ForeignKey(
        PeriodoHistorico, on_delete=models.CASCADE, blank=True, null=True, 
        verbose_name= "Órgão/ Período Histórico" )
    orgao_unidade = models.CharField(max_length=150, verbose_name="Órgão / Unidade")
    sigla = models.CharField(max_length=50)
    tipo_administracao = models.ForeignKey(
        TipoAdminstracao, on_delete=models.CASCADE, blank=True, null=True, 
        verbose_name="Tipo da Administração")
    inicio_vinculo = models.DateField()
    fim_termino = models.DateField(null=True, blank=True)

    orgao_antecessor = models.ForeignKey("self", 
                                         on_delete=models.CASCADE, blank=True, null=True, verbose_name="Vinculo Superior")

    doc_comprovacao = models.FileField(upload_to='fundamentacao/', null=True, blank=True)
    atribuicoes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.orgao_unidade} - {self.sigla}'

# dados sobre o perido historico da parte

class PeriodoHistoricoParte(models.Model):
    denominacao_da_parte = models.CharField(max_length=250, verbose_name="História da Parte")
    organizacao = models.ForeignKey(
        OrgaoUnidade, on_delete=models.CASCADE, blank=True, null=True,
        verbose_name="Orgão do Período")
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    resumo = models.TextField(blank=True, null=True)
    doc_fundamento = models.FileField(upload_to='fundamentacao/', blank=True, null=True)
    obs = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.organizacao} - {self.denominacao_da_parte}'
    class Meta:
        verbose_name_plural = "02 - Faceta História da Parte"


# faceta organizaçao estrutural

class NivelAdmin(models.Model):
    nivel_administrativo = models.CharField(max_length=50)
    descricao = models.TextField()
    def __str__(self):
        return f'{self.nivel_administrativo}'
class Setor(models.Model):
    EXISTENCIA_CHOICES = [
        ("fato", "De Fato"),
        ("direito", "De Direito"),
    ]
    historico_parte = models.ForeignKey(
        PeriodoHistoricoParte, on_delete=models.CASCADE, blank=True, null=True, 
        verbose_name="Historico da Parte")
    nome_setor = models.CharField(max_length=150)
    sigla = models.CharField(max_length=50)

    nivel_admin = models.ForeignKey(
        NivelAdmin, on_delete=models.CASCADE, blank=True, null=True,
        verbose_name="Nivel Administrativo")
    existencia_setor = models.CharField(max_length=10, choices=EXISTENCIA_CHOICES)
    doc_comprovacao = models.FileField(upload_to='fundamentacao/', null=True, blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    unidade_superior = models.ForeignKey(
        "self", 
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        verbose_name="Órgão antecessor")
    atribuicao = models.TextField()
    obs = models.TextField()

    def __str__(self):
        return f'{self.nome_setor} - {self.sigla} - {self.historico_parte}'
    class Meta:
        verbose_name_plural = "03 - Faceta Organico Estrutural"


# faceta funcional

class ConfiguracaoFuncional(models.Model):
    AREA_CHOICES = [
        ("fim", "FIM"),
        ("meio", "MEIO"),
    ]

    EXISTENCIA_CHOICES = [
        ("fato", "De Fato"),
        ("direito", "De Direito"),
    ]

    CONFIGURACAO_FUNCAO = [
        ("função", 'FUNÇÃO'),
        ("sub Função","SUB FUNÇÂO"),
        ("atividade","ATIVIDADE")
    ]

    unidade_administrativa = models.ForeignKey(
        Setor , on_delete=models.CASCADE, blank=True, null=True,
        verbose_name="Unidade Administrativa")
    denominacao = models.CharField(max_length=250)
    arae_atuacao = models.CharField(max_length=10, choices=AREA_CHOICES)
    configuracao_funcional = models.CharField(max_length=10, choices=CONFIGURACAO_FUNCAO)
    existencia = models.CharField(max_length=10, choices=EXISTENCIA_CHOICES )
    doc_comprovacao = models.FileField(upload_to='fundamentacao/', null=True, blank=True)
    atribuicao = models.TextField()
    obs = models.TextField()
    
    def __str__(self):
        return f'{self.denominacao}'
    class Meta:
        verbose_name_plural = "04 - Faceta Funcional"


# faceta Tipo documental

# Essa classe alimenta o preenchimento
# em prazo corrente e intermediario como opçao de escolha


class PrazoDeGuarda(models.Model):
    descricao = models.CharField(max_length=80)
    tempo = models.IntegerField('Quantos anos de guarda')

    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name_plural = "PRAZOS DE GUARDA"
        ordering = ["tempo", 'descricao']

# recebe dados de prazo de guarda
class GuardaCorrente(models.Model):
    # fase corrente
    guarda = models.ForeignKey(PrazoDeGuarda, on_delete=models.CASCADE,
                               blank=True, null=True, verbose_name="Prazo fase corrente")

    def __str__(self):
        return str(self.guarda)
    class Meta:
        verbose_name_plural = "PRAZO DE GUARDAS FASE CORRENTE"
        ordering = ['guarda']

# recebe dados de prazo de guarda
class GuardaIntermediario(models.Model):
    # fase intermediaria
    guarda = models.ForeignKey(PrazoDeGuarda, on_delete=models.CASCADE,
                               blank=True, null=True, verbose_name='Prazo faser intermediaria')

    def __str__(self):
        return str(self.guarda)

    class Meta:
        verbose_name_plural = "PRAZO DE GUARDA FASE INTERMEDIARIA"
        ordering = ['guarda']




# tabela de classificação documental
class ClasseTTDD(models.Model):
    ATIVIDADE_CHOICES = (
        ("ATIVIDADE-FIM", "atividade-fim"),
        ("ATIVIDADE-MEIO", "atividade-meio"),
    )
    atividade_fim = models.CharField(
        "Atividade", max_length=15, choices=ATIVIDADE_CHOICES)
    cod = models.CharField('Código Classificação', max_length=7)
    descricao = models.CharField('Descrição do assunto', max_length=300)
    pai = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True)
    # prazo de guarda
    # fase corrente
    tempo_fase_corrente = models.ForeignKey(
        GuardaCorrente, on_delete=models.CASCADE, blank=True, null=True)

    # fase intermediaria
    tempo_fase_intemediario = models.ForeignKey(
        GuardaIntermediario, on_delete=models.CASCADE, blank=True, null=True)

    # permanente
    DEFINICAO_FINAL_CHOICES = (
        ("GUARDA PERMANENTE", "Guarda Permanente"),
        ("ELIMINAÇÃO", "Eliminação")
    )
    permanente = models.CharField(
        "Destinação,",
        max_length=25, choices=DEFINICAO_FINAL_CHOICES, blank=True, null=True)
    observacao = models.TextField(
        "Observação",
        blank=True, null=True)

    def __str__(self):
        return f'{self.cod} - {self.descricao}'

        # if self.pai is None:
        # # cadastro das Unidades administrativas
        #     return f'{self.cod} - {self.descricao}'
        # else:
        #     return f'{self.cod} - {self.descricao}'
        #- {self.pai}

    class Meta:
        verbose_name_plural = "CLASSIFICAÇÕES TABELA DE TEMPORALIDADE"
        ordering = ['cod']

# Cadastro das epecies documentais utilizada na UFPB
class Especie(models.Model):
    nome = models.CharField('Espécie Documental', max_length=45)
    Descrição = models.TextField(blank=True, null=True,)
    # Selecionar se a especie é de multidocumento ou unitarios
    multiplo = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name_plural = "ESPÉCIES DOCUMENTAIS"


class TermoRemissivo(models.Model):
    termo_remissivo = models.CharField(
        verbose_name="Termo Remissivo", max_length=200)
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.termo_remissivo}'

    class Meta:
        verbose_name_plural = "Termos Remissivos"
        ordering = ['termo_remissivo']


class NormaEspecie(models.Model):
    especie = models.ForeignKey(
        Especie, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Espécie da Norma")
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.especie}'


class NormaTipologia(models.Model):
    especie = models.ForeignKey(
        NormaEspecie, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Espécie")
    norma_tipologia = models.CharField(
        verbose_name="Norma fudamenta tipologia", max_length=200)

    def __str__(self):
        return f'{self.norma_tipologia}'

    class Meta:
        verbose_name_plural = "Normas da tipologia"
        ordering = ['norma_tipologia']


# cadastro dos assuntos
class TipologiaDocumental(models.Model):
    GRAU_SIGILO_CHOICES = (
        ("OSTENSIVO", "Ostensivo"),
        ("RESTRITO", "Restrito"),
    )
    especie = models.ForeignKey(
        Especie, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Espécie")
    tipologia_adotado = models.CharField(max_length=300)

    termo_remissivo = models.ManyToManyField(
        TermoRemissivo)

    norma_tipologia = models.ManyToManyField(NormaTipologia)

    classificacao = models.ForeignKey(
        ClasseTTDD, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Classificação')
    grau_de_acesso = models.CharField(
        max_length=9, choices=GRAU_SIGILO_CHOICES, blank=True, null=True, default='OSTENSIVO')

    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.tipologia_adotado}'

    class Meta:
        verbose_name_plural = "05 - Faceta Tipologia documental"

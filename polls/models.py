from django.db import models
from django.utils import timezone
from datetime import datetime

ENUM_NOMEPRODUTO = (
    ('Gasolina Comum', 'Gasolina Comum'),
    ('Gasolina Aditivada', 'Gasolina Aditivada'),
    ('Álcool Comum', 'Álcool Comum'),
    ('Óleo Diesel Comum', 'Óleo Diesel Comum'),
    ('Óleo Diesel S10', 'Óleo Diesel S10'),
    ('Gás Natural', 'Gás Natural'),
)

ENUM_CARGO = (
    ('Coordenador', 'Coordenador'),
    ('Analista', 'Analista')
)

ENUM_ZONA = (
    ('Norte', 'Norte'),
    ('Sul', 'Sul'),
    ('Leste', 'Leste'),
    ('Oeste', 'Oeste'),
)

ENUM_BAIRRO = (
    ('Água Fria', 'Água Fria'),
    ('Aeroclube', 'Aeroclube'),
    ('Altiplano', 'Altiplano'),
    ('Alto do Céu', 'Alto do Céu'),
    ('Alto do Mateus', 'Alto do Mateus'),
    ('Anatólia', 'Anatólia'),
    ('Bairro das Indústrias', 'Bairro das Indústrias'),
    ('Bairro dos Estados', 'Bairro dos Estados'),
    ('Bairro dos Ipês', 'Bairro dos Ipês'),
    ('Bairro dos Novais','Bairro dos Novais'),
    ('Bancários', 'Bancários'),
    ('Barra de Gramame', 'Barra de Gramame'),
    ('Bessa', 'Bessa'),
    ('Brisamar', 'Brisamar'),
    ('Cabo Branco', 'Cabo Branco'),
    ('Castelo Branco', 'Castelo Branco'),
    ('Centro', 'Centro'),
    ('Cidade dos Colibris', 'Cidade dos Colibris'),
    ('Costa do Sol', 'Costa do Sol'),
    ('Costa e Silva', 'Costa e Silva'),
    ('Cristo Redentor', 'Cristo Redentor'),
    ('Cruz das Armas', 'Cruz das Armas'),
    ('Cuiá', 'Cuiá'),
    ('Distrito Industrial', 'Distrito Industrial'),
    ('Ernesto Geisel', 'Ernesto Geisel'),
    ('Ernâni Sátiro', 'Ernâni Sátiro'),
    ('Expedicionários', 'Expedicionários'),
    ('Funcionários', 'Funcionários'),
    ('Gramame', 'Gramame'),
    ('Grotão', 'Grotão'),
    ('Ilha do Bispo', 'Ilha do Bispo'),
    ('Jaguaribe', 'Jaguaribe'),
    ('Jardim 13 de Maio', 'Jardim 13 de Maio'),
    ('Jardim Cidade Universitária', 'Jardim Cidade Universitária'),
    ('Jardim Esther', 'Jardim Esther'),
    ('Jardim Luna', 'Jardim Luna'),
    ('Jardim Mangueira', 'Jardim Mangueira'),
    ('Jardim Oceania', 'Jardim Oceania'),
    ('Jardim Planalto', 'Jardim Planalto'),
    ('Jardim São Paulo', 'Jardim São Paulo'),
    ('Jardim Veneza', 'Jardim Veneza'),
    ('José Américo', 'José Américo'),
    ('João Agripino', 'João Agripino'),
    ('João Paulo II', 'João Paulo II'),
    ('Manaíra Leste', 'Manaíra Leste'),
    ('Mandacaru', 'Mandacaru'),
    ('Mangabeira', 'Mangabeira'),
    ('Mata do Buraquinho', 'Mata do Buraquinho'),
    ('Miramar', 'Miramar'),
    ('Mumbaba', 'Mumbaba'),
    ('Mussuré', 'Mussuré'),
    ('Muçumagro', 'Muçumagro'),
    ('Oitizeiro', 'Oitizeiro'),
    ('Padre Zé', 'Padre Zé'),
    ('Paratibe', 'Paratibe'),
    ('Pedro Gondim', 'Pedro Gondim'),
    ('Penha Leste', 'Penha Leste'),
    ('Planalto da Boa Esperança', 'Planalto da Boa Esperança'),
    ('Ponta dos Seixas', 'Ponta dos Seixas'),
    ('Portal do Sol', 'Portal do Sol'),
    ('Rangel', 'Rangel'),
    ('Róger', 'Róger'),
    ('São José', 'São José'),
    ('Tambaú', 'Tambaú'),
    ('Tambauzinho', 'Tambauzinho'),
    ('Tambiá', 'Tambiá'),
    ('Torre', 'Torre'),
    ('Trincheiras', 'Trincheiras'),
    ('Valentina Figueiredo', 'Valentina Figueiredo'),
    ('Varadouro', 'Varadouro'),
    ('Varjão', 'Varjão'),
)

ENUM_UF = (
    ('PB', 'PB'),
)

ENUM_CIDADE = (
    ('João Pessoa', 'João Pessoa'),
)

ENUM_TPLOG = (
    ('Aeroporto', 'Aeroporto'),
    ('Alameda', 'Alameda'),
    ('Área', 'Área'),
    ('Avenida', 'Avenida'),
    ('Campo', 'Campo'),
    ('Chácara', 'Chácara'),
    ('Colônia', 'Colônia'),
    ('Condomínio', 'Condomínio'),
    ('Conjunto', 'Conjunto'),
    ('Distrito', 'Distrito'),
    ('Esplanada', 'Esplanada'),
    ('Estação', 'Estação'),
    ('Estrada', 'Estrada'),
    ('Favela', 'Favela'),
    ('Fazenda', 'Fazenda'),
    ('Feira', 'Feira'),
    ('Jardim', 'Jardim'),
    ('Ladeira', 'Ladeira'),
    ('Lago', 'Lago'),
    ('Lagoa', 'Lagoa'),
    ('Largo', 'Largo'),
    ('Loteamento', 'Loteamento'),
    ('Morro', 'Morro'),
    ('Núcleo', 'Núcleo'),
    ('Parque', 'Parque'),
    ('Passarela', 'Passarela'),
    ('Pátio', 'Pátio'),
    ('Praça', 'Praça'),
    ('Quadra', 'Quadra'),
    ('Recanto', 'Recanto'),
    ('Residencial', 'Residencial'),
    ('Rodovia', 'Rodovia'),
    ('Rua', 'Rua'),
    ('Setor', 'Setor'),
    ('Sítio', 'Sítio'),
    ('Travessa', 'Travessa'),
    ('Trecho', 'Trecho'),
    ('Trevo', 'Trevo'),
    ('Vale', 'Vale'),
    ('Vereda', 'Vereda'),
    ('Via', 'Via'),
    ('Viaduto', 'Viaduto'),
    ('Viela', 'Viela'),
    ('Vila', 'Vila'),
)

class Posto(models.Model):
    idPosto = models.AutoField(primary_key=True)
    razaoSocial = models.CharField(max_length=150, verbose_name="Razão Social")
    nomeFantasia = models.CharField(max_length=150, verbose_name="Nome Fantasia")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    cnpj = models.CharField(max_length=14, verbose_name="CNPJ")
    distribuidor = models.CharField(max_length=25, verbose_name="Distribuidor")
    # Endereço
    uf = models.CharField(max_length=2, choices=ENUM_UF, default="PB", verbose_name="UF")
    cidade = models.CharField(max_length=80, choices=ENUM_CIDADE, default="João Pessoa", verbose_name="Cidade")
    bairro = models.CharField(max_length=80, choices=ENUM_BAIRRO, default="Água Fria", verbose_name="Bairro")
    zona = models.CharField(max_length=10, choices=ENUM_ZONA, default="Norte", verbose_name="Zona")
    tpLog = models.CharField(max_length=30, choices=ENUM_TPLOG, default="Rua", verbose_name="Tipo de Logradouro")
    cep =  models.CharField(max_length=8, default="00000000", verbose_name="CEP")
    complemento = models.CharField(max_length=30, default="Marco Zero", verbose_name="Complemento")
    logradouro = models.CharField(max_length=150, default="Travessa ZZZ", verbose_name="Logradouro")
    numero = models.IntegerField(default=10, verbose_name="Número")

    def __str__(self):
        return self.nomeFantasia

    class Meta:
        verbose_name = "Posto de combustíveis"
        verbose_name_plural = "Posto de combustíveis"
        ordering = ('nomeFantasia',)

class Produto(models.Model):
    idProduto = models.AutoField(primary_key=True)
    nome =  models.CharField(max_length=50, choices=ENUM_NOMEPRODUTO, unique=True, null=False, blank=False, verbose_name="Nome do produto")
    postos = models.ManyToManyField(Posto, through='PostoProduto', through_fields=('produto', 'posto'))

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)

class PostoProduto(models.Model):
    #idPP = models.IntergerField(primary_key=True) #Cria-se automaticamente um atributo id
    posto = models.ForeignKey(Posto, on_delete=models.CASCADE, verbose_name="Posto")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name="Produto")

    def __str__(self):
        return str(self.posto) + " - " + str(self.produto)

    class Meta:
        verbose_name = "Produtos por Posto"
        verbose_name_plural = "Produtos por Posto"
        unique_together = ("posto", "produto",)
        ordering = ('posto',)

class Pesquisa(models.Model):
    idPesquisa = models.AutoField(primary_key=True)
    dataPesquisa = models.DateField(null=True, blank=False, unique=True, verbose_name="Data da Pesquisa")
    dataCadastro = models.DateTimeField(default=timezone.now, verbose_name="Data do Cadastro")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    postosEprodutos = models.ManyToManyField(PostoProduto, through='PesquisaPostoProduto', through_fields=('pesquisa', 'postoProduto'))

    def __str__(self):
        return str(self.dataPesquisa)

    class Meta:
        verbose_name = "Pesquisa"
        verbose_name_plural = "Pesquisas"
        ordering = ('dataPesquisa',)

class Pesquisador(models.Model):
    idPesquisador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=15)
    cargo = models.CharField(max_length=50, choices=ENUM_CARGO)
    pesquisas = models.ManyToManyField(Pesquisa, through='PesquisaPesquisadores', through_fields = ('pesquisador', 'pesquisa'))

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pesquisador"
        verbose_name_plural = "Pesquisadores"
        ordering = ('nome',)

class PesquisaPesquisadores(models.Model):
    idPP = models.AutoField(primary_key=True)
    pesquisa = models.ForeignKey(Pesquisa, on_delete=models.CASCADE, verbose_name="Pesquisa")
    pesquisador = models.ForeignKey(Pesquisador, on_delete=models.CASCADE, verbose_name="Pesquisador")

    def __str__(self):
        return str(self.pesquisa)

    class Meta:
        verbose_name = "Pesquisadores por Pesquisa"
        verbose_name_plural = "Pesquisadores por Pesquisa"
        unique_together = ("pesquisa", "pesquisador",)
        ordering = ('pesquisa',)


class PesquisaPostoProduto(models.Model):
    #idPPP = models.IntergerField(primary_key=True) #Cria-se automaticamente um atributo id
    pesquisa = models.ForeignKey(Pesquisa, on_delete=models.CASCADE, verbose_name="Pesquisa")
    postoProduto = models.ForeignKey(PostoProduto, on_delete=models.CASCADE, verbose_name="Posto e Produto")
    precoAvista = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Preço à Vista")
    precoCredito = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Preço Crédito")

    def __str__(self):
        return str(self.pesquisa)

    class Meta:
        verbose_name = "Preços de combustíveis nos postos"
        verbose_name_plural = "Preços de combustíveis nos postos"
        unique_together = ("postoProduto", "pesquisa",)
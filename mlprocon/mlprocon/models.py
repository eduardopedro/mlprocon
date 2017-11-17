from django.db import models

# ENUM_SEXO = (
#        ('-','Selecione'),
#        ('M','MASCULINO'),
#        ('F','FEMININO'),
#)

ENUM_TIPOSDEPRODUTO = (
	('1', 'Alimentos'),
	('2', 'Limpeza'),	
	('3', 'Frios'),
	('4', 'Escritorio'),
)

ENUM_RAMOS = (
	('1', 'Supermercados'),
	('2', 'Textil'),	
	('3', 'Postos de Combustiveis'),
	('4', 'Acougues'),
)

ENUM_TIPOFISC = (
	('1', 'Precos'),
	('2', 'Cumprimento de Lei'),	
)

ENUM_PARECER = (
	('0', 'Regular'),
	('1', 'Irregular'),	
)


class Pesquisas(models.Model):
	idPesquisa = models.IntegerField(null=True, blank=True)
	data = models.DateField(null=True, blank=True)
	descricaoPesquisa = models.CharField(max_length=250)
	responsavel = models.CharField(max_length=50)
    	def __unicode__(self):
       		return self.descricaoPesquisa

class Produtos(models.Model):
	idProduto = models.IntegerField(null=True, blank=True)
	nome = models.CharField(max_length=50)
	descricaoProduto = models.CharField(max_length=250)
	tipoProduto = models.CharField(max_length=20, choices=ENUM_TIPOSDEPRODUTO)
	categoriaProduto = models.CharField(max_length=50)
    	def __unicode__(self):
       		return self.descricaoProduto

class OrgaosFisc(models.Model):
	idOrgao = models.IntegerField(null=True, blank=True)
	nomeOrgao = models.CharField(max_length=50) 
	email = models.CharField(max_length=50)
	nomeContato = models.CharField(max_length=50)
	telefone = models.CharField(max_length=15)
	diretor = models.CharField(max_length=50)
	telefoneContato = models.CharField(max_length=15)
	endereco = models.CharField(max_length=150)
	def __unicode__(self):
       		return self.nomeOrgao

class Empresas(models.Model):
	idEmpresa = models.IntegerField(null=True, blank=True)
	endereco = models.CharField(max_length=150)
	ramo = models.CharField(max_length=20, choices=ENUM_RAMOS)
	cnpj = models.CharField(max_length=18)
	telefone = models.CharField(max_length=15)
	nome = models.CharField(max_length=50)
	nomeFantasia = models.CharField(max_length=50)
	def __unicode__(self):
       		return self.nome
	
class OrgaoPesquisa(models.Model):
	#idOrgao = models.IntegerField(null=True, blank=True)
	#idPesquisa = models.IntegerField(null=True, blank=True)
	idOrgao = models.ForeignKey(OrgaosFisc)
 	idPesquisa = models.ForeignKey(Pesquisas)
    	def __unicode__(self):
      		return self.idOrgao

class ProdutosEmpresas(models.Model):
	#idEmpresa = models.IntegerField(null=True, blank=True)
	#idProduto = models.IntegerField(null=True, blank=True)
	idEmpresa = models.ForeignKey(Empresas)
	idProduto = models.ForeignKey(Produtos)	
	def __unicode__(self):
      		return self.idEmpresa

class ProdEmpPesq(models.Model):
	#idPesquisa = models.IntegerField(null=True, blank=True)
	#idEmpresa = models.IntegerField(null=True, blank=True)
	#idProduto = models.IntegerField(null=True, blank=True)
	preco = models.DecimalField(max_digits=10, decimal_places=2)
	idPesquisa = models.ForeignKey(Pesquisas)
	idEmpresa = models.ForeignKey(Empresas)
	idProduto = models.ForeignKey(Produtos)
	def __unicode__(self):
      		return self.preco

class Fiscalizacoes(models.Model):
	#idOrgao = models.IntegerField(null=True, blank=True)
	#idEmpresa = models.IntegerField(null=True, blank=True)
	idFisc = models.IntegerField(null=True, blank=True)	
	data = models.DateField(null=True, blank=True)
	descricaoFiscalizacao = models.CharField(max_length=250)
	parecer = models.CharField(max_length=20, choices=ENUM_PARECER)
	observacao = models.CharField(max_length=250)
	tipoFiscalizacao = models.CharField(max_length=20, choices=ENUM_TIPOFISC)
	idOrgao = models.ForeignKey(OrgaosFisc)
	idEmpresa = models.ForeignKey(Empresas)
	def __unicode__(self):
      		return self.descricaoFiscalizacao


#class TipoRemedio(models.Model):
#    codigoTipo = models.IntegerField(null=True, blank=True)
#    descricaoTipo   = models.CharField(max_length=50)
#    def __unicode__(self):
#       return self.descricaoTipo

#class Remedio(models.Model):
#    codigoRemedio = models.IntegerField(null=True, blank=True)
#    descricao  = models.CharField(max_length=50)
#    composicao = models.CharField(max_length=60)
#    valorUnit  = models.FloatField(null=True, blank=True)
#    tiporemedio = models.ForeignKey(TipoRemedio)
#    def __unicode__(self):
#       return self.descricao

#class Medico(models.Model):
#    CRM   = models.CharField(max_length=30)
#    Nome  = models.CharField(max_length=70)
#    Email = models.CharField(max_length=90)
#    def __unicode__(self):
#       return self.Nome

#class Paciente(models.Model):
#    codigo = models.IntegerField(null=True, blank=True)
#    nome_Paciente = models.CharField(max_length=50)
#   email = models.CharField(max_length=90)
#    fone = models.CharField(max_length=50)
#    def __unicode__(self):
#    	return self.nome_Paciente

##class ProntuarioEletronico(models.Model):
#    codigoProntuario = models.IntegerField(null=True, blank=True)
#    descricaoProntuario = models.CharField(max_length=60)
#    dosagem = models.CharField(max_length=40)
#    qtdvezesdia = models.IntegerField(null=True, blank=True)
#    datainicio = models.DateField(null=True, blank=True)
#    qtddias = models.IntegerField(null=True, blank=True)
#    obs = models.CharField(max_length=100)
 #   medico = models.ForeignKey(Medico)
 #   remedio = models.ForeignKey(Remedio)
#    paciente = models.ForeignKey(Paciente)
#    def ___unicode__(self):
#        return self.descricaoProntuario

#class PlanilhaHorarios(models.Model):
#    descricao = models.CharField(max_length=50)
#    data = models.DateField(null=True, blank=True)
 #   hora = models.TimeField(null=True, blank=True)
 #   prontuario = models.ForeignKey(ProntuarioEletronico)
 #   def __unicode__(self):
 #       return self.descricao

#class Professor(models.Model):
 #  nome = models.CharField(max_length=50)
 #  idade = models.IntegerField(null=True, blank=True)
 #  def __unicode__(self):
#	return self.nome


































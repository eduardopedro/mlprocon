#from contatos.models import ENUM_SEXO, TipoRemedio, Remedio, Medico, Paciente, ProntuarioEletronico, PlanilhaHorarios, Professor
#from django.contrib import admin

#admin.site.register(TipoRemedio)
#admin.site.register(Remedio)
#admin.site.register(Medico)
#admin.site.register(Paciente)
#admin.site.register(ProntuarioEletronico)
#admin.site.register(PlanilhaHorarios)
#admin.site.register(Professor)

from contatos.models import ENUM_TIPOSDEPRODUTO, ENUM_RAMOS, ENUM_TIPOFISC, ENUM_PARECER, Pesquisas, Produtos, OrgaosFisc, Empresas, OrgaoPesquisa, ProdutosEmpresas, ProdEmpPesq, Fiscalizacoes
from django.contrib import admin

admin.site.register(Pesquisas)
admin.site.register(Produtos)
admin.site.register(OrgaosFisc)
admin.site.register(Empresas)
admin.site.register(OrgaoPesquisa)
admin.site.register(ProdutosEmpresas)
admin.site.register(ProdEmpPesq)
admin.site.register(Fiscalizacoes)



from django.contrib import admin
from django.contrib.admin import TabularInline

from .models import Posto
from .models import Produto
from .models import PostoProduto
from .models import Pesquisa
from .models import Pesquisador
from .models import PesquisaPesquisadores
from .models import PesquisaPostoProduto


class PesquisadorAdmin(admin.ModelAdmin):

    search_fields = ('nome','telefone', 'cargo',)
    list_per_page = 10
    fieldsets = [
        (None, {'fields': [('nome', 'telefone'), 'cargo',]}),
    ]
    list_display = ['nome', 'telefone', 'cargo',]


class PesquisaPesquisadoresAdmin(admin.ModelAdmin):

    search_fields = ('pesquisa__dataPesquisa','pesquisador__nome',)
    list_per_page = 10
    fieldsets = [
        (None, {'fields': ['pesquisa','pesquisador',]}),
    ]
    list_display = ['pesquisa','pesquisador',]


class PesquisaAdmin(admin.ModelAdmin):

    search_fields = ('dataPesquisa','descricao',)
    list_per_page = 10
    fieldsets = [
        (None, {'fields': ['dataPesquisa','descricao',]}),
    ]
    #inlines = [PesquisaPostoProdutoInline],
    list_display = ['dataPesquisa','descricao',]


class PostoAdmin(admin.ModelAdmin):

    search_fields = ('nomeFantasia', 'distribuidor', 'zona', 'bairro', 'logradouro')
    list_per_page = 10
    fieldsets = [
        (None, {'fields': ['razaoSocial','nomeFantasia', 'telefone', 'cnpj', 'distribuidor']}),
        ('Endereço', {'fields': [('uf', 'cidade', 'bairro'), ('zona', 'tpLog', 'cep'), 'complemento',('logradouro', 'numero')]}),
    ]
    list_display = ['nomeFantasia', 'distribuidor', 'zona', 'bairro', 'logradouro']


#class PostoProdutoInline(admin.TabularInline):
#    model = PostoProduto
#    extra = 6
    #show_change_link = True


class PesquisaPostoProdutoAdmin(admin.ModelAdmin):

    search_fields = ('pesquisa__dataPesquisa','postoProduto__posto__nomeFantasia', 'postoProduto__produto__nome', 'precoAvista', 'precoCredito')
    list_per_page = 10
    fieldsets = [
        (None, {'fields': ['pesquisa',]}),
        ('Informe os preços', {'fields':[('postoProduto', 'precoAvista', 'precoCredito'),], 'classes': ['collapse']}),
    ]
    #inlines = [PostoProdutoInline],
    #list_editable = ['precoAvista', 'precoCredito'],
    list_display = ['pesquisa', 'postoProduto', 'precoAvista', 'precoCredito']

class ProdutoAdmin(admin.ModelAdmin):

    search_fields = ('nome',)
    list_per_page = 10
    fieldsets = [
        (None, {'fields': ['nome']}),
    ]
    list_display = ['nome',]

class PostoProdutoAdmin(admin.ModelAdmin):

    search_fields = ('posto__nomeFantasia','produto__nome',)
    list_per_page = 10
    fieldsets = [
        (None, {'fields': ['posto','produto',]}),
    ]
    list_display = ['posto','produto',]

admin.site.register(Posto, PostoAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(PostoProduto, PostoProdutoAdmin)
admin.site.register(Pesquisa, PesquisaAdmin)
admin.site.register(Pesquisador, PesquisadorAdmin)
admin.site.register(PesquisaPesquisadores, PesquisaPesquisadoresAdmin)
admin.site.register(PesquisaPostoProduto, PesquisaPostoProdutoAdmin)

# Register your models here.

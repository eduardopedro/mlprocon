# Generated by Django 2.0.3 on 2018-03-14 23:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pesquisa',
            fields=[
                ('idPesquisa', models.AutoField(primary_key=True, serialize=False)),
                ('dataPesquisa', models.DateField(null=True, unique=True, verbose_name='Data da Pesquisa')),
                ('dataCadastro', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data do Cadastro')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Pesquisa',
                'verbose_name_plural': 'Pesquisas',
                'ordering': ('dataPesquisa',),
            },
        ),
        migrations.CreateModel(
            name='Pesquisador',
            fields=[
                ('idPesquisador', models.AutoField(primary_key=True, serialize=False)),
                ('telefone', models.CharField(max_length=15)),
                ('nome', models.CharField(max_length=150)),
                ('cargo', models.CharField(choices=[('1', 'Coordenador'), ('2', 'Analista')], max_length=50)),
            ],
            options={
                'verbose_name': 'Pesquisador',
                'verbose_name_plural': 'Pesquisadores',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='PesquisaPesquisadores',
            fields=[
                ('idPP', models.AutoField(primary_key=True, serialize=False)),
                ('pesquisa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Pesquisa', verbose_name='Pesquisa')),
                ('pesquisador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Pesquisador', verbose_name='Pesquisador')),
            ],
            options={
                'verbose_name': 'Pesquisadores por Pesquisa',
                'verbose_name_plural': 'Pesquisadores por Pesquisa',
            },
        ),
        migrations.CreateModel(
            name='PesquisaPostoProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precoAvista', models.DecimalField(decimal_places=3, max_digits=5, verbose_name='Preço à Vista')),
                ('precoCredito', models.DecimalField(decimal_places=3, max_digits=5, verbose_name='Preço Crédito')),
                ('pesquisa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Pesquisa', verbose_name='Pesquisa')),
            ],
            options={
                'verbose_name': 'Preços de combustíveis nos postos',
                'verbose_name_plural': 'Preços de combustíveis nos postos',
            },
        ),
        migrations.CreateModel(
            name='Posto',
            fields=[
                ('idPosto', models.AutoField(primary_key=True, serialize=False)),
                ('razaoSocial', models.CharField(max_length=150, verbose_name='Razão Social')),
                ('nomeFantasia', models.CharField(max_length=150, verbose_name='Nome Fantasia')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('distribuidor', models.CharField(max_length=25, verbose_name='Distribuidor')),
            ],
            options={
                'verbose_name': 'Posto de combustíveis',
                'verbose_name_plural': 'Posto de combustíveis',
                'ordering': ('nomeFantasia',),
            },
        ),
        migrations.CreateModel(
            name='PostoProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Produtos por Posto',
                'verbose_name_plural': 'Produtos por Posto',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('idProduto', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(choices=[('1', 'Gasolina Comum'), ('2', 'Gasolina Aditivada'), ('3', 'Álcool Comum'), ('4', 'Óleo Diesel Comum'), ('5', 'Óleo Diesel S10'), ('6', 'Gás Natural')], max_length=50, verbose_name='Nome do produto')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('uf', models.CharField(choices=[('1', 'PB')], max_length=2, verbose_name='UF')),
                ('cidade', models.CharField(choices=[('1', 'João Pessoa')], max_length=80, verbose_name='Cidade')),
                ('bairro', models.CharField(choices=[('1', 'Água Fria'), ('2', 'Aeroclube'), ('3', 'Altiplano'), ('4', 'Alto do Céu'), ('5', 'Alto do Mateus'), ('6', 'Anatólia'), ('7', 'Bairro das Indústrias'), ('8', 'Bairro dos Estados'), ('9', 'Bairro dos Ipês'), ('10', 'Bairro dos Novais'), ('11', 'Bancários'), ('12', 'Barra de Gramame'), ('13', 'Bessa'), ('14', 'Brisamar'), ('15', 'Cabo Branco'), ('16', 'Castelo Branco'), ('17', 'Centro'), ('18', 'Cidade dos Colibris'), ('19', 'Costa do Sol'), ('20', 'Costa e Silva'), ('21', 'Cristo Redentor'), ('22', 'Cruz das Armas'), ('23', 'Cuiá'), ('24', 'Distrito Industrial'), ('25', 'Ernesto Geisel'), ('26', 'Ernâni Sátiro'), ('27', 'Expedicionários'), ('28', 'Funcionários'), ('29', 'Gramame'), ('30', 'Grotão'), ('31', 'Ilha do Bispo'), ('32', 'Jaguaribe'), ('33', 'Jardim 13 de Maio'), ('34', 'Jardim Cidade Universitária'), ('35', 'Jardim Esther'), ('36', 'Jardim Luna'), ('37', 'Jardim Mangueira'), ('38', 'Jardim Oceania'), ('39', 'Jardim Planalto'), ('40', 'Jardim São Paulo'), ('41', 'Jardim Veneza'), ('42', 'José Américo'), ('43', 'João Agripino'), ('44', 'João Paulo II'), ('45', 'Manaíra Leste'), ('46', 'Mandacaru'), ('47', 'Mangabeira'), ('48', 'Mata do Buraquinho'), ('49', 'Miramar'), ('50', 'Mumbaba'), ('51', 'Mussuré'), ('52', 'Muçumagro'), ('53', 'Oitizeiro'), ('54', 'Padre Zé'), ('55', 'Paratibe'), ('56', 'Pedro Gondim'), ('57', 'Penha Leste'), ('58', 'Planalto da Boa Esperança'), ('59', 'Ponta dos Seixas'), ('60', 'Portal do Sol'), ('61', 'Rangel'), ('62', 'Róger'), ('63', 'São José'), ('64', 'Tambaú'), ('65', 'Tambauzinho'), ('66', 'Tambiá'), ('67', 'Torre'), ('68', 'Trincheiras'), ('69', 'Valentina Figueiredo'), ('70', 'Varadouro'), ('71', 'Varjão')], max_length=80, verbose_name='Bairro')),
                ('zona', models.CharField(choices=[('1', 'Norte'), ('2', 'Sul'), ('3', 'Leste'), ('4', 'Oeste')], max_length=10, verbose_name='Zona')),
                ('tpLog', models.CharField(choices=[('1', 'Aeroporto'), ('2', 'Alameda'), ('3', 'Área'), ('4', 'Avenida'), ('5', 'Campo'), ('6', 'Chácara'), ('7', 'Colônia'), ('8', 'Condomínio'), ('9', 'Conjunto'), ('10', 'Distrito'), ('12', 'Esplanada'), ('13', 'Estação'), ('14', 'Estrada'), ('15', 'Favela'), ('16', 'Fazenda'), ('17', 'Feira'), ('18', 'Jardim'), ('19', 'Ladeira'), ('20', 'Lago'), ('21', 'Lagoa'), ('22', 'Largo'), ('23', 'Loteamento'), ('24', 'Morro'), ('25', 'Núcleo'), ('26', 'Parque'), ('27', 'Passarela'), ('28', 'Pátio'), ('29', 'Praça'), ('30', 'Quadra'), ('31', 'Recanto'), ('32', 'Residencial'), ('33', 'Rodovia'), ('34', 'Rua'), ('35', 'Setor'), ('36', 'Sítio'), ('37', 'Travessa'), ('38', 'Trecho'), ('39', 'Trevo'), ('40', 'Vale'), ('41', 'Vereda'), ('42', 'Via'), ('43', 'Viaduto'), ('44', 'Viela'), ('45', 'Vila')], max_length=30, verbose_name='Tipo de Logradouro')),
                ('cep', models.CharField(max_length=8, verbose_name='CEP')),
                ('complemento', models.CharField(max_length=30, verbose_name='Complemento')),
                ('logradouro', models.CharField(max_length=150, verbose_name='Logradouro')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('posto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='polls.Posto')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
                'ordering': ('zona', 'bairro'),
            },
        ),
        migrations.AddField(
            model_name='produto',
            name='postos',
            field=models.ManyToManyField(through='polls.PostoProduto', to='polls.Posto'),
        ),
        migrations.AddField(
            model_name='postoproduto',
            name='posto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Posto', verbose_name='Posto'),
        ),
        migrations.AddField(
            model_name='postoproduto',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Produto', verbose_name='Produto'),
        ),
        migrations.AddField(
            model_name='pesquisapostoproduto',
            name='postoProduto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.PostoProduto', verbose_name='Posto e Produto'),
        ),
        migrations.AddField(
            model_name='pesquisador',
            name='pesquisas',
            field=models.ManyToManyField(through='polls.PesquisaPesquisadores', to='polls.Pesquisa'),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='postosEprodutos',
            field=models.ManyToManyField(through='polls.PesquisaPostoProduto', to='polls.PostoProduto'),
        ),
        migrations.AlterUniqueTogether(
            name='postoproduto',
            unique_together={('posto', 'produto')},
        ),
        migrations.AlterUniqueTogether(
            name='pesquisapostoproduto',
            unique_together={('postoProduto', 'pesquisa')},
        ),
    ]

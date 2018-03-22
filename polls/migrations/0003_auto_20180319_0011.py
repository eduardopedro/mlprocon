# Generated by Django 2.0.3 on 2018-03-19 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180318_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='posto',
        ),
        migrations.AddField(
            model_name='posto',
            name='bairro',
            field=models.CharField(choices=[('Água Fria', 'Água Fria'), ('Aeroclube', 'Aeroclube'), ('Altiplano', 'Altiplano'), ('Alto do Céu', 'Alto do Céu'), ('Alto do Mateus', 'Alto do Mateus'), ('Anatólia', 'Anatólia'), ('Bairro das Indústrias', 'Bairro das Indústrias'), ('Bairro dos Estados', 'Bairro dos Estados'), ('Bairro dos Ipês', 'Bairro dos Ipês'), ('Bairro dos Novais', 'Bairro dos Novais'), ('Bancários', 'Bancários'), ('Barra de Gramame', 'Barra de Gramame'), ('Bessa', 'Bessa'), ('Brisamar', 'Brisamar'), ('Cabo Branco', 'Cabo Branco'), ('Castelo Branco', 'Castelo Branco'), ('Centro', 'Centro'), ('Cidade dos Colibris', 'Cidade dos Colibris'), ('Costa do Sol', 'Costa do Sol'), ('Costa e Silva', 'Costa e Silva'), ('Cristo Redentor', 'Cristo Redentor'), ('Cruz das Armas', 'Cruz das Armas'), ('Cuiá', 'Cuiá'), ('Distrito Industrial', 'Distrito Industrial'), ('Ernesto Geisel', 'Ernesto Geisel'), ('Ernâni Sátiro', 'Ernâni Sátiro'), ('Expedicionários', 'Expedicionários'), ('Funcionários', 'Funcionários'), ('Gramame', 'Gramame'), ('Grotão', 'Grotão'), ('Ilha do Bispo', 'Ilha do Bispo'), ('Jaguaribe', 'Jaguaribe'), ('Jardim 13 de Maio', 'Jardim 13 de Maio'), ('Jardim Cidade Universitária', 'Jardim Cidade Universitária'), ('Jardim Esther', 'Jardim Esther'), ('Jardim Luna', 'Jardim Luna'), ('Jardim Mangueira', 'Jardim Mangueira'), ('Jardim Oceania', 'Jardim Oceania'), ('Jardim Planalto', 'Jardim Planalto'), ('Jardim São Paulo', 'Jardim São Paulo'), ('Jardim Veneza', 'Jardim Veneza'), ('José Américo', 'José Américo'), ('João Agripino', 'João Agripino'), ('João Paulo II', 'João Paulo II'), ('Manaíra Leste', 'Manaíra Leste'), ('Mandacaru', 'Mandacaru'), ('Mangabeira', 'Mangabeira'), ('Mata do Buraquinho', 'Mata do Buraquinho'), ('Miramar', 'Miramar'), ('Mumbaba', 'Mumbaba'), ('Mussuré', 'Mussuré'), ('Muçumagro', 'Muçumagro'), ('Oitizeiro', 'Oitizeiro'), ('Padre Zé', 'Padre Zé'), ('Paratibe', 'Paratibe'), ('Pedro Gondim', 'Pedro Gondim'), ('Penha Leste', 'Penha Leste'), ('Planalto da Boa Esperança', 'Planalto da Boa Esperança'), ('Ponta dos Seixas', 'Ponta dos Seixas'), ('Portal do Sol', 'Portal do Sol'), ('Rangel', 'Rangel'), ('Róger', 'Róger'), ('São José', 'São José'), ('Tambaú', 'Tambaú'), ('Tambauzinho', 'Tambauzinho'), ('Tambiá', 'Tambiá'), ('Torre', 'Torre'), ('Trincheiras', 'Trincheiras'), ('Valentina Figueiredo', 'Valentina Figueiredo'), ('Varadouro', 'Varadouro'), ('Varjão', 'Varjão')], default='Água Fria', max_length=80, verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='posto',
            name='cep',
            field=models.CharField(default='00000000', max_length=8, verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='posto',
            name='cidade',
            field=models.CharField(choices=[('João Pessoa', 'João Pessoa')], default='João Pessoa', max_length=80, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='posto',
            name='complemento',
            field=models.CharField(default='Marco Zero', max_length=30, verbose_name='Complemento'),
        ),
        migrations.AddField(
            model_name='posto',
            name='logradouro',
            field=models.CharField(default='Travessa ZZZ', max_length=150, verbose_name='Logradouro'),
        ),
        migrations.AddField(
            model_name='posto',
            name='numero',
            field=models.IntegerField(default=10, verbose_name='Número'),
        ),
        migrations.AddField(
            model_name='posto',
            name='tpLog',
            field=models.CharField(choices=[('Aeroporto', 'Aeroporto'), ('Alameda', 'Alameda'), ('Área', 'Área'), ('Avenida', 'Avenida'), ('Campo', 'Campo'), ('Chácara', 'Chácara'), ('Colônia', 'Colônia'), ('Condomínio', 'Condomínio'), ('Conjunto', 'Conjunto'), ('Distrito', 'Distrito'), ('Esplanada', 'Esplanada'), ('Estação', 'Estação'), ('Estrada', 'Estrada'), ('Favela', 'Favela'), ('Fazenda', 'Fazenda'), ('Feira', 'Feira'), ('Jardim', 'Jardim'), ('Ladeira', 'Ladeira'), ('Lago', 'Lago'), ('Lagoa', 'Lagoa'), ('Largo', 'Largo'), ('Loteamento', 'Loteamento'), ('Morro', 'Morro'), ('Núcleo', 'Núcleo'), ('Parque', 'Parque'), ('Passarela', 'Passarela'), ('Pátio', 'Pátio'), ('Praça', 'Praça'), ('Quadra', 'Quadra'), ('Recanto', 'Recanto'), ('Residencial', 'Residencial'), ('Rodovia', 'Rodovia'), ('Rua', 'Rua'), ('Setor', 'Setor'), ('Sítio', 'Sítio'), ('Travessa', 'Travessa'), ('Trecho', 'Trecho'), ('Trevo', 'Trevo'), ('Vale', 'Vale'), ('Vereda', 'Vereda'), ('Via', 'Via'), ('Viaduto', 'Viaduto'), ('Viela', 'Viela'), ('Vila', 'Vila')], default='Rua', max_length=30, verbose_name='Tipo de Logradouro'),
        ),
        migrations.AddField(
            model_name='posto',
            name='uf',
            field=models.CharField(choices=[('PB', 'PB')], default='PB', max_length=2, verbose_name='UF'),
        ),
        migrations.AddField(
            model_name='posto',
            name='zona',
            field=models.CharField(choices=[('Norte', 'Norte'), ('Sul', 'Sul'), ('Leste', 'Leste'), ('Oeste', 'Oeste')], default='Norte', max_length=10, verbose_name='Zona'),
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
    ]

from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Properties, Album, Client
import pytz


@login_required()
def imoveis(request):
    imoveis = Properties.objects.order_by('-data_disponivel')
    clientes = Client.objects.order_by('data_cadastro')
    tipoimoveis = Properties.TIPOIMOVEL

    dados = {
        'clientes': clientes,
        'imoveis': imoveis,
        'tiposimoveis': tipoimoveis,
        'segment': 'imoveis'
    }

    return render(request, 'properties/imoveis.html', dados)


@login_required()
def criaimoveis(request):
    data = datetime.now(pytz.timezone('America/Sao_Paulo'))

    if request.method == 'POST':
        id_usuario = get_object_or_404(User, pk=request.user.id)
        tipo_imovel = request.POST['tipo_imovel']
        cep = request.POST['cep']
        logradouro = request.POST['logradouro']
        numero = request.POST['numero']
        complemento = request.POST['complemento']
        bairro = request.POST['bairro']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        descricao = request.POST['descricao']
        preco = request.POST['preco']
        aluguel = request.POST.get('aluguel', False)
        compra = request.POST.get('compra', False)
        venda = request.POST.get('venda', False)
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        numeroquartos = request.POST['nquartos']
        numerobanheiros = request.POST['nbanheiros']
        vagasgaragem = request.POST['nvagasgaragem']
        areatotal = request.POST['areatotal']
        areaconstruida = request.POST['areaconstruida']
        data_cadastro = data
        data_atualizacao = data
        data_disponivel = data
        cliente = get_object_or_404(Client, pk=request.POST['cliente'])
        foto_capa = request.FILES.get('capa', None)
        fotos = request.FILES.getlist('imagens')
        ativo = request.POST.get('ativo', False)

        """Valida Aluguel, Compra e Venda"""
        aluguel = True if aluguel == 'on' else False
        compra = True if compra == 'on' else False
        venda = True if venda == 'on' else False
        ativo = True if ativo == 'on' else False

        imoveis = Properties.objects.create(id_usuario=id_usuario, tipo_imovel=tipo_imovel,
                                            cep=cep, logradouro=logradouro, numero=numero,
                                            complemento=complemento, bairro=bairro,
                                            cidade=cidade, estado=estado, descricao=descricao,
                                            preco=preco, aluguel=aluguel, compra=compra,
                                            venda=venda, latitude=latitude, longitude=longitude,
                                            numeroquartos=numeroquartos, numerobanheiros=numerobanheiros,
                                            vagasgaragem=vagasgaragem, areatotal=areatotal,
                                            areaconstruida=areaconstruida, data_cadastro=data_cadastro,
                                            data_atualizacao=data_atualizacao, data_disponivel=data_disponivel,
                                            cliente=cliente, foto_capa=foto_capa, ativo=ativo)

        imoveis.save()
        id_imoveis = get_object_or_404(Properties, pk=imoveis.pk)

        """ Inclusão do Album """
        for foto in fotos:
            album = Album.objects.create(id_imovel=id_imoveis, imagem=foto)
            album.save()

        messages.success(request, "Imóvel incluído com sucesso!")
        return redirect('imoveis')
    else:
        clientes = Client.objects.order_by('data_cadastro')

        dados = {
            'clientes': clientes,
            'segment': 'imoveis'
        }

        return render(request, 'properties/cria_imoveis.html', dados)


@login_required()
def atualizaimoveis(request):
    """ Atualiza Imóvel """
    data = datetime.now(pytz.timezone('America/Sao_Paulo'))
    if request.method == 'POST':
        imovel = Properties.objects.get(pk=request.POST.get('id'))
        imovel.id_usuario = get_object_or_404(User, pk=request.user.id)
        imovel.tipo_imovel = request.POST['tipo_imovel']
        imovel.cep = request.POST['cep']
        imovel.logradouro = request.POST['logradouro']
        imovel.numero = request.POST['numero']
        imovel.complemento = request.POST['complemento']
        imovel.bairro = request.POST['bairro']
        imovel.cidade = request.POST['cidade']
        imovel.estado = request.POST['estado']
        imovel.descricao = request.POST['descricao']
        imovel.preco = request.POST['preco']
        imovel.aluguel = request.POST.get('aluguel', False)
        imovel.compra = request.POST.get('compra', False)
        imovel.venda = request.POST.get('venda', False)
        imovel.latitude = request.POST['latitude']
        imovel.longitude = request.POST['longitude']
        imovel.numeroquartos = request.POST['nquartos']
        imovel.numerobanheiros = request.POST['nbanheiros']
        imovel.vagasgaragem = request.POST['nvagasgaragem']
        imovel.areatotal = request.POST['areatotal']
        imovel.areaconstruida = request.POST['areaconstruida']
        imovel.data_atualizacao = data
        imovel.data_disponivel = data
        imovel.ativo = request.POST.get('ativo', False)
        imovel.cliente = get_object_or_404(Client, pk=request.POST['cliente'])
        imovel.foto_capa = request.FILES.get('capa', imovel.foto_capa)

        """ Inclusão do Album """
        fotos = request.FILES.getlist('imagens')
        for foto in fotos:
            album = Album.objects.create(id_imovel=imovel, imagem=foto)
            album.save()

        """Valida Aluguel, Compra e Venda"""
        imovel.aluguel = True if imovel.aluguel == 'on' else False
        imovel.compra = True if imovel.compra == 'on' else False
        imovel.venda = True if imovel.venda == 'on' else False
        imovel.ativo = True if imovel.ativo == 'on' else False

        imovel.save()
        messages.success(request, "Imóvel atualizado com sucesso!")
        return redirect('imoveis')
    else:
        return redirect('imoveis')


@login_required()
def deletaimoveis(request, idimoveis):
    """ Delete Imóvel """
    imoveis = get_object_or_404(Properties, pk=idimoveis)
    imoveis.delete()
    messages.success(request, 'Imóvel deletadao com sucesso!')
    return redirect('imoveis')
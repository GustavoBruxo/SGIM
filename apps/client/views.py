from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Client, Category


@login_required(login_url="/login/")
def clientes(request):
    clientes = Client.objects.filter(ativo=True).order_by('-data_cadastro')

    """Valida e Categoria Tipo de Pessoa"""
    for cliente in clientes:
        if cliente.tipo_pessoa == 'PF':
            cliente.tipo_pessoa = 'Física'
        else:
            cliente.tipo_pessoa = 'Jurídica'

    dados = {
        'clientes': clientes,
        'segment': 'clientes'
    }

    return render(request, 'client/clientes.html', dados)

@login_required(login_url="/login/")
def criacliente(request):
    if request.method == 'POST':
        """Inclui um operação"""
        categoria = request.POST['categoria']
        tipo_pessoa = request.POST['pessoa']
        aluguel = request.POST.get('aluguel', False)
        compra = request.POST.get('compra', False)
        venda = request.POST.get('venda', False)
        nomecliente = request.POST['nome']
        cpf_cnjp = request.POST['cpfcnpj']
        telefone = request.POST['telefone']
        email = request.POST['email']
        cep = request.POST['cep']
        logradouro = request.POST['logradouro']
        numero = request.POST['numero']
        complemento = request.POST['complemento']
        bairro = request.POST['bairro']
        cidade =request.POST['cidade'] 
        estado = request.POST['estado']
        observacao = request.POST['observacao']
        anexo = request.FILES.get('anexo', None)
        usuario = get_object_or_404(User, pk=request.user.id)
        data_cadastro = datetime.now()

        """Valida Categoria"""
        categoria = get_object_or_404(Category, pk=categoria)
        
        """Valida Tipo de Pessoa"""
        if tipo_pessoa == 'Física':
            tipo_pessoa = 'PF'
        else:
            tipo_pessoa = 'PJ'

        """Valida Aluguel, Compra e Venda"""
        if aluguel == 'on':
            aluguel = True
        if compra == 'on':
            compra = True
        if venda == 'on':
            venda = True

        cliente = Client.objects.create(categoria=categoria, tipo_pessoa=tipo_pessoa,
                                        aluguel=aluguel, compra=compra, venda=venda,
                                        nomecliente=nomecliente, cpf_cnjp=cpf_cnjp,
                                        telefone=telefone, email=email, cep=cep,
                                        logradouro=logradouro, numero=numero,
                                        complemento=complemento, bairro=bairro,
                                        cidade=cidade, estado=estado,
                                        observacao=observacao, anexo=anexo,
                                        usuario=usuario,data_cadastro=data_cadastro)

        cliente.save()
        messages.success(request, "Cliente incluído com sucesso!")
        return redirect('clientes')
    else:
        categoria = Category.objects.order_by('categoria').filter(ativo=True)
        dados = {
            'categorias': categoria,
            'segment': 'clientes'
        }
        return render(request, 'client/cria_cliente.html', dados)


@login_required(login_url="/login/")
def deletacliente(request, idcliente):
    """Deleta um cliente"""
    cliente =get_object_or_404(Client, pk=idcliente)
    cliente.delete()
    messages.success(request, 'Cliente deletadao com sucesso!')
    return redirect('clientes')


@login_required(login_url="/login/")
def consultacliente(request, idcliente):
    """Edita a cliente selecionado"""
    cliente = Client.objects.get(id=idcliente)
    categorias = Category.objects.order_by('-id')
    
    """Valida Tipo Pessoa"""
    if cliente.tipo_pessoa == 'PF':
        cliente.tipo_pessoa = 'Física'
    else:
        cliente.tipo_pessoa = 'Jurídica'

    dados = {
        'cliente': cliente,
        'categoria': categorias,
        'segment': 'clientes'
    }

    return render(request, 'client/consulta_cliente.html', dados)


@login_required(login_url="/login/")
def editacliente(request, idcliente):
    """Edita a cliente selecionado"""
    cliente = Client.objects.get(id=idcliente)
    categorias = Category.objects.order_by('-id')
    
    """Valida Tipo Pessoa"""
    if cliente.tipo_pessoa == 'PF':
        cliente.tipo_pessoa = 'Física'
    else:
        cliente.tipo_pessoa = 'Jurídica'

    dados = {
        'cliente': cliente,
        'categoria': categorias,
        'segment': 'clientes'
    }

    return render(request, 'client/edita_cliente.html', dados)


@login_required(login_url="/login/")
def atualizacliente(request):
    """Atualiza a cliente"""
    if request.method == 'POST':
        cliente = Client.objects.get(pk=request.POST.get('id'))
        categoria = request.POST['categoria']
        cliente.tipo_pessoa = request.POST['pessoa']
        cliente.aluguel = request.POST.get('aluguel', False)
        cliente.compra = request.POST.get('compra', False)
        cliente.venda = request.POST.get('venda', False)
        cliente.nomecliente = request.POST['nome']
        cliente.cpf_cnjp = request.POST['cpfcnpj']
        cliente.telefone = request.POST['telefone']
        cliente.email = request.POST['email']
        cliente.cep = request.POST['cep']
        cliente.logradouro = request.POST['logradouro']
        cliente.numero = request.POST['numero']
        cliente.complemento = request.POST['complemento']
        cliente.bairro = request.POST['bairro']
        cliente.cidade =request.POST['cidade'] 
        cliente.estado = request.POST['estado']
        cliente.observacao = request.POST['observacao']
        cliente.anexo = request.FILES.get('anexo', None)
        cliente.usuario = get_object_or_404(User, pk=request.user.id)
        cliente.data_cadastro = datetime.now()

        """Valida Categoria"""
        categorys = Category.objects.order_by('-data_cadastro')
        for category in categorys:
            if category.categoria == categoria:
                cliente.categoria = get_object_or_404(Category, pk=category.id)
        
        """Valida Tipo de Pessoa"""
        if cliente.tipo_pessoa == 'Física':
            cliente.tipo_pessoa = 'PF'
        else:
            cliente.tipo_pessoa = 'PJ'

        """Valida Aluguel, Compra e Venda"""
        if cliente.aluguel == 'on':
            cliente.aluguel = True
        if cliente.compra == 'on':
            cliente.compra = True
        if cliente.venda == 'on':
            cliente.venda = True

        cliente.save()
        messages.success(request, "Cliente atualizado com sucesso!")
        return redirect('clientes')
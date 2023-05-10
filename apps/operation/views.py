from django.shortcuts import get_object_or_404, redirect, render
from .models import Operation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

@login_required(login_url="/")
def operacoes(request):
    operacoes = Operation.objects.order_by('-data_operacao')

    total_entrada = 0
    qtde_entrada = 0
    total_saida = 0
    qtde_saida = 0

    for operacao in operacoes:
        if operacao.tipo_operacao == 'ENT':
            total_entrada += operacao.valor
            qtde_entrada += 1
        else:
            total_saida += operacao.valor
            qtde_saida += 1

    dados = {
        'operacoes': operacoes,
        'segment': 'operacoes'
    }
    return render(request, 'operation/operacoes.html', dados)


@login_required(login_url="/")
def criaoperacao(request):
    if request.method == 'POST':
        """Inclui um operação"""
        descricao = request.POST['descricao']
        anexo = request.FILES['anexo']
        valor = float(request.POST['valor'])
        data_operacao = request.POST['data_operacao']
        tipo_operacao = request.POST['tipo_operacao']
        usuario = get_object_or_404(User, pk=request.user.id)

        """Valida a operação"""
        for idoperacao, operacao in Operation.TIPO:
            if operacao == tipo_operacao:
                tipo_operacao = idoperacao

        operacao = Operation.objects.create(descricao=descricao,
                                            anexo=anexo,
                                            valor=valor,
                                            data_operacao=data_operacao,
                                            tipo_operacao=tipo_operacao,
                                            usuario=usuario)

        operacao.save()
        messages.success(request, "Operação incluída com sucesso!")
        return redirect('operacoes')
    else:
        return render(request, 'operation/cria_operacao.html')


@login_required(login_url="/")
def deletaoperacao(request, idoperacao):
    """Deleta uma operação"""
    operacao = get_object_or_404(Operation, pk=idoperacao)
    operacao.delete()
    messages.success(request, 'Operação deletada com sucesso!')
    return redirect('operacoes')


@login_required(login_url="/")
def editaoperacao(request, idoperacao):
    """Edita a operação selecionada"""
    operacao = Operation.objects.get(id=idoperacao)

    valor = str(operacao.valor).replace(',', '.')
    operacao.valor = valor

    dados = {
        'operacao': operacao,
        'segment': 'operacoes'
    }
    return render(request, 'operation/edita_operacao.html', dados)


@login_required(login_url="/")
def atualizaoperacao(request):
    """Atualiza a operação"""
    if request.method == 'POST':
        a = Operation.objects.get(pk=request.POST.get('id'))
        a.descricao = request.POST['descricao']
        a.valor = request.POST['valor']
        a.data_operacao = request.POST['data_operacao']
        a.tipo_operacao = request.POST['tipo_operacao']

        """Valida a operação"""
        for idoperacao, operacao in Operation.TIPO:
            if operacao == a.tipo_operacao:
                a.tipo_operacao = idoperacao

        if 'anexo' in request.FILES:
            a.anexo = request.FILES['anexo']

        a.save()
        messages.success(request, "Operação atualizada com sucesso!")
        return redirect('operacoes')

from django.shortcuts import render, redirect
from operation.models import Operation
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url="/")
def home(request):
    ano_atual = date.today().year
    mes_atual = date.today().month
    operacao = Operation.objects.filter(data_operacao__year=ano_atual,data_operacao__month=mes_atual).order_by('-data_operacao')

    dados = {
        'operacoes': operacao,
        'segment': 'home'
    }

    return render(request, 'sgim/index.html', dados)
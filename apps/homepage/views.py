from django.shortcuts import render, redirect
from properties.models import Properties

# Create your views here.


def home(request):
    imoveis = Properties.objects.order_by('-data_disponivel').filter(ativo=True)

    dados = {
        'imoveis': imoveis,
        'segment': 'home'
    }

    return render(request, 'sgim/home.html', dados)
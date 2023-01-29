from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Properties, Album


@login_required(login_url="/")
def imoveis(request):

    dados = {
        'segment': 'imoveis'
    }

    return render(request, 'properties/imoveis.html', dados)

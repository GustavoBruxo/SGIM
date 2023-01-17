from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages


def cadastro(request):
    """Cadastra uma nova pessoa no sistema """
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco!')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco!')
            return redirect('cadastro')

        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais!')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('cadastro')

        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('cadastro')

        user = User.objects.create_user(
            username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'user/cadastro.html')


def login(request):
    """Realiza o login de uma pessoa no sistema"""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'E-mail ou senha inválidos. Tente novamente!')
            return redirect('login')
                
    return render(request, 'user/login.html')


def logout(request):
    """Realiza o logout do usuário do site"""
    auth.logout(request)
    return redirect('login')


def campo_vazio(campo):
    """Valida se o campo do formulário esta vazio"""
    return not campo.strip()


def senhas_nao_sao_iguais(senha, senha2):
    """Valida se as senhas são diferentes"""
    return senha != senha2

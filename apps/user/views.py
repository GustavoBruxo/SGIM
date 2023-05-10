from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator


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


def reset(request):
    """ Reseta a senha do usuário """
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            print('A1')
        except User.DoesNotExist:
            messages.error(request, 'Este e-mail não está associado a nenhuma conta.')
            print('A2')
            return redirect('reset')

        # Generate a one-time use token and a link to reset the password
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        reset_link = request.build_absolute_uri(
            reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token}))
        # Send the password reset email
        email_subject = 'Redefinição de senha'
        email_body = render_to_string('user/email/password_reset_email.html', {
            'user': user,
            'reset_link': reset_link,
            'site_name': settings.SITE_NAME
        })
        email = EmailMessage(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [email]
        )
        email.send()
        messages.success(request, 'Foi enviado um e-mail com instruções para redefinir sua senha.')
        return redirect('login')
    print('A3')
    return render(request=request, template_name='user/password_reset_request.html')


def campo_vazio(campo):
    """Valida se o campo do formulário esta vazio"""
    return not campo.strip()


def senhas_nao_sao_iguais(senha, senha2):
    """Valida se as senhas são diferentes"""
    return senha != senha2

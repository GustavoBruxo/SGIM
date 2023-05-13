from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from properties.models import Properties

# Create your views here.


@login_required(login_url="login/")
def home(request):
    imoveis = Properties.objects.order_by('-data_disponivel').filter(ativo=True)

    dados = {
        'imoveis': imoveis,
        'segment': 'home'
    }
    return render(request, 'sgim/home.html', dados)
    

@login_required(login_url="login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        return render(request, 'sgim/page-404.html')

    except:
        return render(request, 'sgim/page-500.html')
        
#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Category, Client

# Register your models here.


class ListandoCategory(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'ativo', 'data_cadastro',)
    list_display_links = ('id', 'categoria',)
    search_fields = ('categoria',)
    list_per_page = 30


admin.site.register(Category, ListandoCategory)


class ListandoClients(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'tipo_pessoa','ativo', 'nomecliente','cpf_cnjp',
                    'email',)
    list_display_links = ('id', 'categoria', 'tipo_pessoa','ativo', 'nomecliente','cpf_cnjp',
                    'email',)
    search_fields = ('categoria', 'tipo_pessoa','ativo', 'nomecliente','cpf_cnjp',
                    'email',)
    list_per_page = 30

    fieldsets = (
        ('Dados do Cliente', {
            'fields': ('tipo_pessoa', 'categoria','nomecliente',
                'cpf_cnjp', 'telefone','email','ativo',)
        }),
        ('Endereço', {
            'classes': ('wide',),
            'fields': ('cep', 'logradouro','numero','complemento',
                'bairro','cidade','estado',)
        })
    )


admin.site.register(Client, ListandoClients)
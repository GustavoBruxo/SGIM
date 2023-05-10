from django.contrib import admin
from .models import Properties

# Register your models here.


class ListandoProperties(admin.ModelAdmin):
    list_display = ('id', 'id_usuario', 'tipo_imovel','cep', 'logradouro','numero',
                    'complemento','bairro', 'cidade', 'estado', 'descricao', 'preco', 'aluguel',
                    'compra', 'venda', 'latitude', 'longitude', 'ativo')
    list_display_links = ('id', 'id_usuario', 'tipo_imovel','cep', 'logradouro','numero',
                    'complemento','bairro', 'cidade', 'estado', 'descricao', 'preco', 'aluguel',
                    'compra', 'venda', 'latitude', 'longitude', 'ativo')
    search_fields = ('id_usuario', 'tipo_imovel','cep', 'logradouro','numero',
                    'complemento','bairro', 'cidade', 'estado', 'descricao', 'preco', 'aluguel',
                    'compra', 'venda', 'latitude', 'longitude', 'ativo')
    list_per_page = 30

    fieldsets = (
        ('Dados do Cliente', {
            'fields': ('id_usuario', 'tipo_imovel', 'preco', 'ativo',
                'aluguel', 'compra', 'venda', 'latitude', 'longitude', 'cliente', 'foto_capa')
        }),
        ('Endereço', {
            'classes': ('wide',),
            'fields': ('cep', 'logradouro','numero','complemento',
                'bairro','cidade','estado', 'numeroquartos', 'numerobanheiros',
                'vagasgaragem', 'areatotal', 'areaconstruida', 'data_cadastro',
                'data_atualizacao', 'data_disponivel')
        })
    )


admin.site.register(Properties, ListandoProperties)
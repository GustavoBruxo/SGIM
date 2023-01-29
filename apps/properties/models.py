from django.db import models
from django.contrib.auth.models import User
from client.models import Client
# Create your models here.


class Properties(models.Model):
    TIPOIMOVEL = (
        ('CS','Casa'),
        ('AP','Apartamento'),
        ('TR','Terreno'),
        ('GL','Galpão'),
        ('IN','Industria'),
        ('RU','Rural')
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_imovel = models.CharField(max_length=2, choices=TIPOIMOVEL, blank=False, null=False)
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=256)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    descricao = models.TextField()
    preco =  models.DecimalField(max_digits=10, decimal_places=2)
    aluguel = models.BooleanField(default=False)
    compra = models.BooleanField(default=False)
    venda = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=10, decimal_places=10)
    longitude = models.DecimalField(max_digits=10, decimal_places=10)
    numeroquartos = models.IntegerField(null=True)
    numerobanheiros = models.IntegerField(null=True)
    areatotal = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    areaconstruida = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    data_cadastro = models.DateTimeField()
    data_atualizacao = models.DateTimeField()
    data_disponivel = models.DateTimeField()
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)



class Album(models.Model):
    imovel = models.ForeignKey(Properties, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='album/%m/%Y/', blank=True)

# It creates a table in the database with the fields specified in the class.
from django.db import models
# Importing the User model from the Django authentication system.
from django.contrib.auth.models import User


# The Category class is a model that has a categoria field, an ativo field, and a data_cadastro field
class Category(models.Model):
    categoria = models.CharField(max_length=100)
    ativo = models.BooleanField()
    data_cadastro = models.DateTimeField()

    def __str__(self):
        return self.categoria.strip()

    class Meta:
        verbose_name_plural = 'Categorias'


# It creates a table in the database with the fields specified in the class.
class Client(models.Model):
    TIPOPESSOA = (
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica')
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    tipo_pessoa = models.CharField(max_length=2, choices=TIPOPESSOA, blank=False, null=False)
    ativo = models.BooleanField(default=True)
    nomecliente = models.CharField(max_length=256)
    cpf_cnjp = models.CharField(max_length=20)
    telefone = models.CharField(max_length=16)
    email = models.EmailField(max_length=256)
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=256)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    observacao = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    aluguel = models.BooleanField(default=False)
    compra = models.BooleanField(default=False)
    venda = models.BooleanField(default=False)
    anexo = models.ImageField(upload_to='anexo/%m/%Y/', blank=True)

    def __str__(self):
        return self.nomecliente

    class Meta:
        verbose_name_plural = 'Clientes'

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Operation(models.Model):
    TIPO = (
        ('ENT', 'Entrada'),
        ('SAI', 'Saída')
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=256)
    anexo = models.ImageField(upload_to='anexo/%m/%Y/', blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_operacao = models.DateTimeField()
    tipo_operacao = models.CharField(max_length=3, choices=TIPO, blank=False, null=False)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = 'Operações'

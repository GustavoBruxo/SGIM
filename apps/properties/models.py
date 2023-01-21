from django.db import models

# Create your models here.

class Properties(models.Model):
    TIPOIMOVEL = (
        ('CS','Casa'),
        ('AP','Apartamento'),
        ('LT','Lote'),
        ('GL','Galpão'),
        ('','')
    )
# Generated by Django 4.1.3 on 2023-01-10 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_remove_category_observacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='aluguel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='compra',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='venda',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]

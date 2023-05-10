from django.contrib import admin
from .models import Operation

# Register your models here.


class ListandoOperation(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor',
                    'data_operacao', 'tipo_operacao')
    list_display_links = ('id', 'descricao', 'valor')
    list_per_page = 30


admin.site.register(Operation, ListandoOperation)

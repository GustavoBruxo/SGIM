from django.urls import path
from .views import *

urlpatterns = [
    path('operacoes/', operacoes, name='operacoes'),
    path('operacao/criaoperacao/', criaoperacao, name='criaoperacao'),
    path('operacao/deleta/<int:idoperacao>/', deletaoperacao, name='deletaoperacao'),
    path('operacao/edita/<int:idoperacao>/', editaoperacao, name='editaoperacao'),
    path('operacao/atualiza/', atualizaoperacao, name='atualizaoperacao'),
]

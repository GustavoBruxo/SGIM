from django.urls import path
from .views import *

urlpatterns = [
    path('cliente/', clientes, name='clientes'),
    path('cliente/criacliente/', criacliente, name='criacliente'),
    path('cliente/deleta/<int:idcliente>/', deletacliente, name='deletacliente'),
    path('cliente/edita/<int:idcliente>/', editacliente, name='editacliente'),
    path('cliente/consulta/<int:idcliente>/', consultacliente, name='consultacliente'),
    path('cliente/atualiza/', atualizacliente, name='atualizacliente')
]

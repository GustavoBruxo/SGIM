from django.urls import path
from .views import *

urlpatterns = [
    path('imoveis/', imoveis, name='imoveis'),
    path('imoveis/criaimoveis/', criaimoveis, name='criaimoveis'),
    path('imoveis/deleta/<int:idimoveis>/', deletaimoveis, name='deletaimoveis'),
    path('imoveis/atualiza/', atualizaimoveis, name='atualizaimoveis'),
]
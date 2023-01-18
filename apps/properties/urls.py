from django.urls import path
from .views import *

urlpatterns = [
    path('imoveis', imoveis, name='imoveis'),
]
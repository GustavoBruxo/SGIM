from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    # Matches any html file
    #re_path(r'^.*\.*', pages, name='pages'),
]
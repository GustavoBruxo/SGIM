from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('reset/', views.reset, name='reset'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/login.html'), name='password_reset_complete')
]

from django.urls import path
from .views import PaginaPerfil
from django.contrib.auth import views as auth_view
from .views import CriarConta

app_name = 'usuarios'
urlpatterns = [
    path('editarperfil/', PaginaPerfil.as_view() , name="editarperfil" ),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='usuariologin'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='usuariologout'),
    path('criarconta/', CriarConta.as_view(template_name='criarconta.html'), name='criarconta'),
    ]

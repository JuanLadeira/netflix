from django.urls import path, reverse_lazy
from .views import PaginaPerfil
from django.contrib.auth import views as auth_view
from .views import CriarConta

app_name = 'usuarios'
urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('criarconta/', CriarConta.as_view(template_name='criarconta.html'), name='criarconta'),
    path('editarperfil/<int:pk>/', PaginaPerfil.as_view() , name="editarperfil" ),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html',
                        success_url = reverse_lazy(['filmes:homefilme'])) , name="mudarsenha" ),
    ]

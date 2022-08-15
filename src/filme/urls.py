from django.urls import path, include
from .views import  HomePage , HomeFilme, DetalhesFilme, PesquisaFilme

app_name = 'filmes'
urlpatterns = [
    path('', HomePage.as_view() , name='homepage'),
    path('filmes', HomeFilme.as_view() , name='homefilme'),
    path('filmes/<int:pk>/', DetalhesFilme.as_view() , name='detalhefilme'),
    path('pesquisa', PesquisaFilme.as_view() , name='pesquisafilme'),
    path('usuario', include('usuario.urls', namespace='usuarios'))
]

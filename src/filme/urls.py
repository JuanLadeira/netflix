from django.urls import path, include
from .views import  HomePage , HomeFilme, DetalhesFilme
urlpatterns = [
    path('', HomePage.as_view() , name='home-filme'),
    path('filmes/', HomeFilme.as_view() , name='home-page'),
    path('filmes/<int:pk>/', DetalhesFilme.as_view() , name='detalhe-filme'),
]

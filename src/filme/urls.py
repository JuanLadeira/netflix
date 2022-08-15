from django.urls import path
from .views import  HomePage , HomeFilme, DetalhesFilme

app_name = 'filmes'
urlpatterns = [
    path('', HomePage.as_view() , name='homepage'),
    path('filmes', HomeFilme.as_view() , name='homefilme'),
    path('filmes/<int:pk>/', DetalhesFilme.as_view() , name='detalhefilme'),
]

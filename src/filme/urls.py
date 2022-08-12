from django.urls import path, include
from .views import homepage, HomePage , HomeFilme
urlpatterns = [
    path('', HomePage.as_view() , name='home-filme'),
    path('filmes/', HomeFilme.as_view() , name='home-page'),
]

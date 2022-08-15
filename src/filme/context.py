#GERENCIADOR DE CONTEXTO.
from .models import Filme

def lista_filmes_recentes(request):
    """
    Lista de Filmes recentes "-data_criacao" ordem decrescente, do mais novo ao mais antigo.
    """
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:5] 
    return {"filmes_recentes": lista_filmes}

def lista_filmes_em_alta(request):
    """
    Lista de filmes em alta "-visualizacoes" ordem decrescente
    """
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:5] 
    return {"filmes_em_alta": lista_filmes}
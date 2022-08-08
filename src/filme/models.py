from distutils.command.upload import upload
from django.db import models

LISTA_CATEGORIAS = (
    ("ANALISES", 'Análises'),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros")
    )

# Create your models here.
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to="thumb_filmes")
    descricao = models.TextField()
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
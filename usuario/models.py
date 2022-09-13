from django.db import models
from django.contrib.auth.models import AbstractUser
from filme.models import Filme

# Create your models here.
class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField(Filme, related_name='Filmes')

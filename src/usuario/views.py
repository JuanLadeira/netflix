from re import T
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class PaginaPerfil(TemplateView):
    template_name = "perfilusuario.html"
    
from re import T
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class PaginaPerfil(LoginRequiredMixin, TemplateView):
    template_name = "perfilusuario.html"

class CriarConta(TemplateView):
    template_name = "criarconta.html"

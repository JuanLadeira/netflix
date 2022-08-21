from re import T
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaUsuario



# Create your views here.

class PaginaPerfil(LoginRequiredMixin, TemplateView):
    template_name = "perfilusuario.html"

class CriarConta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaUsuario
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('usuarios:login')

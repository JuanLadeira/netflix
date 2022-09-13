from django.shortcuts import render, reverse
from django.views.generic import  FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaUsuario
from .models import Usuario


# Create your views here.

class PaginaPerfil(LoginRequiredMixin, UpdateView):
    template_name = "perfilusuario.html"
    model = Usuario
    fields = ['first_name','last_name','email','password', ]

    def get_success_url(self):
        return reverse('filmes:homefilme')   


class CriarConta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaUsuario
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('usuarios:login')


    

from multiprocessing import context
from tkinter.messagebox import RETRY
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Filme
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class HomePage(TemplateView):
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        usuario = request.user
        if usuario.is_authenticated:
            return redirect("filmes:homefilme")
        return super().get(request, *args, **kwargs)

class HomeFilme(LoginRequiredMixin, ListView):
    template_name = 'homefilme.html'
    model = Filme

class DetalhesFilme(LoginRequiredMixin, DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme

    def get(self, request, *args, **kwargs):
        #contabilizando vizualiação
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetalhesFilme,self).get_context_data(**kwargs)
        if filmes_relacionados:
            filmes_relacionados =  self.model.objects.filter(categoria=self.get_object().categoria)[0:5] #filtrando todos os objetos que pertencem a mesma categoria
            context['filmes_relacionados'] = filmes_relacionados
        return context

class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name ='pesquisa.html'
    model = Filme

    def get_queryset(self):
        pesquisa = self.request.GET.get('query')
        if pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=pesquisa)
            return object_list
        else: 
            return None
#def homepage(request):
#    obj = Filme.objects.all()
#    context = {
#        'obj': obj
#    }
#    return render(request, 'homefilme.html' , context)
from gc import get_objects
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Filme

# Create your views here.

class HomePage(TemplateView):
    template_name = 'homepage.html'

class HomeFilme(ListView):
    template_name = 'homefilme.html'
    model = Filme

class DetalhesFilme(DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme

    def get(self, request, *args, **kwargs):
        #contabilizando vizualiação
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetalhesFilme,self).get_context_data(**kwargs)
        filmes_relacionados =  Filme.objects.filter(categoria=self.get_object().categoria)[0:5] #filtrando todos os objetos que pertencem a mesma categoria
        context['filmes_relacionados'] = filmes_relacionados
        return context


#def homepage(request):
#    obj = Filme.objects.all()
#    context = {
#        'obj': obj
#    }
#    return render(request, 'homefilme.html' , context)
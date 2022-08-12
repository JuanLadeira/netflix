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

#def homepage(request):
#    obj = Filme.objects.all()
#    context = {
#        'obj': obj
#    }
#    return render(request, 'homefilme.html' , context)
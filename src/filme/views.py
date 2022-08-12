from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Filme

# Create your views here.

class HomePage(TemplateView):
    template_name = 'homefilme.html'

def homepage(request):
    obj = Filme.objects.all()
    context = {
        'obj': obj
    }
    return render(request, 'homefilme.html' , context)
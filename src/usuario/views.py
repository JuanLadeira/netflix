from django.shortcuts import render

# Create your views here.

def templateview(request):
    return render(request, "main.html", {})
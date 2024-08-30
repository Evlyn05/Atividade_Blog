from django.shortcuts import render
from .models import*

# Create your views here.

def index(request):
    euevlyn = Eu.objects.all()
    dados = {
        'Catalogo':  euevlyn,
    }
    return render(request, 'blog/index.html',dados)

def sobre_eu(request):
    euevlyn = Eu.objects.all()
    dados = {
        'Catalogo':  euevlyn,
    }
    return render(request, 'blog/sobre.html',dados)

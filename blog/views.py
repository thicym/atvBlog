from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Curso, Interesse, SobreMim

def sobre_mim(request):
    sobre = SobreMim.objects.first()
    return render(request, 'sobre_mim.html', {'sobre': sobre})

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def interesses(request):
    interesses = Interesse.objects.all()
    return render(request, 'interesses.html', {'interesses': interesses})

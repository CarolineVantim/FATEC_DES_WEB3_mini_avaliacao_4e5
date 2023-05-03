from django.shortcuts import render
from .models import FeriadoModel
import datetime

data = datetime.date.today()
qs = a.objects.all()
def atividade(request):
    for f in qs:
        if f.dia == data.day and f.mes == data.month:
            contexto = {
                'nome': f.nome
            }
            return render(request, 'index.html', contexto)
    else:
        contexto = {
            'nome': False
        }
        return render(request, 'index.html', contexto)
    
def cadastro(request):
    return render(request, 'cadastro.html')
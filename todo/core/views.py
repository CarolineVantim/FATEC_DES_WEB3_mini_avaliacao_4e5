from django.shortcuts import render
from .models import AtividadeModel
from django.utils import timezone
import datetime

dataatual = datetime.date.today()
qs = AtividadeModel.objects.all()

def atividade(request):
    for a in qs:
        data = a.data
        if data.day == dataatual.day and data.month == dataatual.month and data.year == dataatual.year:
            contexto = {
                'nome': a.nome,
                'descricao': a.descricao
            }
            return render(request, 'index.html', contexto)
    else:
        contexto = {
            'nome': False
        }
        return render(request, 'index.html', contexto)
    
def cadastro(request):
    return render(request, 'cadastro.html')
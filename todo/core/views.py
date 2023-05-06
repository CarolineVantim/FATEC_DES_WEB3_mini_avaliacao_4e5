from django.shortcuts import render
from .models import AtividadeModel
from .forms import AtividadeForm
from django.utils import timezone
import datetime

dataatual = datetime.date.today()
qs = AtividadeModel.objects.all()

def atividade(request):
    atividades = {}
    for a in qs:
        data = a.data
        if data.day == dataatual.day and data.month == dataatual.month and data.year == dataatual.year:
            atividades[a.nome] = a.descricao

    if len(atividades)>0:
        contexto = {
            'atividades': atividades
        }
        return render(request, 'index.html', contexto)
    else:
        contexto = {
            'atividades': False
        }
        return render(request, 'index.html', contexto)
    

def cadastro(request):
    if request.method == 'POST':
        form = AtividadeForm(request.POST)

        if form.is_valid():
            AtividadeModel.objects.create(**form.cleaned_data)
            contexto = {
                'cadastro': True
            }
            return render(request, "cadastro.html", contexto)
        else:
            contexto = {'form': form}
            return render(request, "cadastro.html", contexto)
    else:
        contexto = {'form': AtividadeForm}
        return render(request, "cadastro.html", contexto)

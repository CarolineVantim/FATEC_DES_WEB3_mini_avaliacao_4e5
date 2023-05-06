from django import forms
from .models import AtividadeModel
from django.forms import ModelForm

class AtividadeForm(ModelForm):

    class Meta:
        model = AtividadeModel
        fields = ['nome','descricao','data']
        widgets = {
            'data': forms.DateInput(
                attrs={'type': 'date'}
            )
        }
        error_messages = {
        'nome': {
            'required': ("Informe o nome da atividade."),
        },
        'data': {
            'required': ("Informe a data dessa atividade."),
        }
    }

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data
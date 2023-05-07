from django.db import models
from django.utils import timezone

class AtividadeModel(models.Model):
    nome = models.CharField('Nome',max_length=100)
    descricao = models.CharField('Descricao', max_length=500,blank=True)
    data = models.DateField(verbose_name='Data')
    modificado_em = models.DateTimeField(verbose_name='modificado em',auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Atividades'
        verbose_name = 'Atividade'
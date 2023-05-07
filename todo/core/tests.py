from django.test import TestCase
from core.models import AtividadeModel
from django.utils import timezone

class AtividadeModelTest(TestCase):
    def setUp(self):
        self.atividade = AtividadeModel.objects.create(
            nome='Atividade Teste',
            descricao='Descrição da atividade de teste',
            data=timezone.now())

    def test_str(self):
        self.assertEqual(str(self.atividade), 'Atividade Teste')

    def test_verbose_names(self):
        self.assertEqual(AtividadeModel._meta.verbose_name_plural, 'Atividades')
        self.assertEqual(AtividadeModel._meta.verbose_name, 'Atividade')

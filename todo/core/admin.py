from django.contrib import admin
from .models import AtividadeModel

class AtividadeModelAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao','data','modificado_em')
    date_hierarchy = 'modificado_em'
    search_fields = ('nome','descricao','data','modificado_em')
    list_filter = ('modificado_em',)


admin.site.register(AtividadeModel, AtividadeModelAdmin)


# Register your models here.

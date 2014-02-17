# coding: utf-8

from django.contrib import admin
from drisapp.core.models import Norma, HistoricoUsuarios

class NormaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dados Gerais', {'fields': ['cultura', 'regiao', 'epoca', 'ativo']}),
        ('Média', {'fields': ['n_m', 'p_m', 'k_m', 'ca_m', 'mg_m', 's_m', 'b_m', 'cu_m', 'fe_m', 'mn_m', 'zn_m']}),
        ('Desvio Padrão', {'fields': ['n_dp', 'p_dp', 'k_dp', 'ca_dp', 'mg_dp', 's_dp', 'b_dp', 'cu_dp', 'fe_dp', 'mn_dp', 'zn_dp']})
    ]
    list_display = ('cultura', 'regiao', 'epoca', 'ativo')

class HistoricoUsuariosAdmin(admin.ModelAdmin):
    list_display = ('proprietario', 'propriedade', 'horario')

admin.site.register(Norma, NormaAdmin)
admin.site.register(HistoricoUsuarios, HistoricoUsuariosAdmin)



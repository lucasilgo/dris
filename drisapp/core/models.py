# coding: utf-8

from django.db import models

class Norma(models.Model):
    #Campos de identificação
    cultura = models.CharField(max_length=255)
    regiao = models.CharField(max_length=255)
    epoca = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)
    #Campos de média
    n_m = models.CharField(max_length=255)
    p_m = models.CharField(max_length=255)
    k_m = models.CharField(max_length=255)
    ca_m = models.CharField(max_length=255)
    mg_m = models.CharField(max_length=255)
    s_m = models.CharField(max_length=255)
    b_m = models.CharField(max_length=255)
    cu_m = models.CharField(max_length=255)
    fe_m = models.CharField(max_length=255)
    mn_m = models.CharField(max_length=255)
    zn_m = models.CharField(max_length=255)
    #Campos de desvio padrão
    n_dp = models.CharField(max_length=255)
    p_dp = models.CharField(max_length=255)
    k_dp = models.CharField(max_length=255)
    ca_dp = models.CharField(max_length=255)
    mg_dp = models.CharField(max_length=255)
    s_dp = models.CharField(max_length=255)
    b_dp = models.CharField(max_length=255)
    cu_dp = models.CharField(max_length=255)
    fe_dp = models.CharField(max_length=255)
    mn_dp = models.CharField(max_length=255)
    zn_dp = models.CharField(max_length=255)

    def __unicode__(self):
        return (self.cultura + self.regiao + self.epoca)

class HistoricoUsuarios(models.Model):
    proprietario = models.CharField(max_length=255)
    propriedade = models.CharField(max_length=255)
    horario = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.proprietario
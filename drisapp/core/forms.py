# coding: utf-8

from django import forms
from django.utils.translation import ugettext as _
from drisapp.core.models import Norma

class CalculateForm(forms.Form):
    n = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Unidade: g/Kg'}))
    p = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Unidade: g/Kg'}))
    k = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Unidade: g/Kg'}))
    ca = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Unidade: g/Kg'}))
    mg = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Unidade: g/Kg'}))
    s = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Unidade: g/Kg'}))
    b = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Unidade: mg/Kg'}))
    cu = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Unidade: mg/Kg'}))
    fe = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Unidade: mg/Kg'}))
    mn = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Unidade: mg/Kg'}))
    zn = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Unidade: mg/Kg'}))
    proprietario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quem é o dono da propriedade?'}))
    propriedade = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Qual o nome da propriedade?'}))
    lavoura = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Qual o tipo da lavoura?'}))
    cultura = forms.ModelChoiceField(queryset=Norma.objects.filter(ativo=True), empty_label='-', widget=forms.Select(attrs={'class': 'form-control'}))
    amostra = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quem o tipo da amostra?'}))
    data_coleta = forms.DateField(label=('Data da Coleta'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quando a coleta foi feita? Ex: 12/02/2014'}))
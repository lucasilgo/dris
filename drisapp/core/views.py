# coding: utf-8

from django.shortcuts import render
from drisapp.core.forms import CalculateForm
from drisapp.core.models import Norma, HistoricoUsuarios

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def calculate(request):
    if request.method == 'POST':
        form = CalculateForm(request.POST)
        if form.is_valid():
            form_dict = form.cleaned_data.copy()
            aux = calculate_dris(form.cleaned_data)
            form_dict['chart'] = aux
            HistoricoUsuarios(proprietario=form_dict['proprietario'], propriedade=form_dict['propriedade']).save()
            return render(request, 'relatorio.html', form_dict)
        else:
            return render(request, 'calculate.html', {'form': form})
    return render(request, 'calculate.html', {'form': CalculateForm()})

def calculate_dris(form):
    media, dp, dados, rel = [], [], [], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    aux = 0
    # Monta a lista de médias da norma
    media.append(converte_string_lista(form['cultura'].n_m))
    media.append(converte_string_lista(form['cultura'].p_m))
    media.append(converte_string_lista(form['cultura'].k_m))
    media.append(converte_string_lista(form['cultura'].ca_m))
    media.append(converte_string_lista(form['cultura'].mg_m))
    media.append(converte_string_lista(form['cultura'].s_m))
    media.append(converte_string_lista(form['cultura'].b_m))
    media.append(converte_string_lista(form['cultura'].cu_m))
    media.append(converte_string_lista(form['cultura'].fe_m))
    media.append(converte_string_lista(form['cultura'].mn_m))
    media.append(converte_string_lista(form['cultura'].zn_m))
    # Monta a lista de desvio padrão da norma
    dp.append(converte_string_lista(form['cultura'].n_dp))
    dp.append(converte_string_lista(form['cultura'].p_dp))
    dp.append(converte_string_lista(form['cultura'].k_dp))
    dp.append(converte_string_lista(form['cultura'].ca_dp))
    dp.append(converte_string_lista(form['cultura'].mg_dp))
    dp.append(converte_string_lista(form['cultura'].s_dp))
    dp.append(converte_string_lista(form['cultura'].b_dp))
    dp.append(converte_string_lista(form['cultura'].cu_dp))
    dp.append(converte_string_lista(form['cultura'].fe_dp))
    dp.append(converte_string_lista(form['cultura'].mn_dp))
    dp.append(converte_string_lista(form['cultura'].zn_dp))
    # Monta a lista de dados da coleta
    dados.append(float(form['n']))
    dados.append(float(form['p']))
    dados.append(float(form['k']))
    dados.append(float(form['ca']))
    dados.append(float(form['mg']))
    dados.append(float(form['s']))
    dados.append(float(form['b']))
    dados.append(float(form['cu']))
    dados.append(float(form['fe']))
    dados.append(float(form['mn']))
    dados.append(float(form['zn']))
    # Monta a base do gráfico aqui
    for i in range(11):
        for j in range(11):
            rel[i] += (dados[i]/dados[j] - media[i][j]) * (10/dp[i][j])
        rel[i] = str(round(rel[i] / 21, 2))
    # Cálculo IBN
    for i in rel:
        aux += float(i)
    rel.append(str(round(aux / 11, 2)))
    return rel

def converte_string_lista(string):
    return [float(x) for x in string.split(', ')]
